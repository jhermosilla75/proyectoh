# treeview

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo
from evento import Evento
import csv

class App(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.parent= parent
        # definimos 2 columnas 1: tabla, 2: barra de desplazamiento
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0) # wight=0 no cambia de tamaño nunca
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)


        # definimos las columnas de la tabla
        columnas = ("lunes", "martes", "miercoles", "jueves", "viernes")

        self.tabla = ttk.Treeview(self, columns=columnas, show='headings', selectmode="browse") # sin multi-seleccion
        self.tabla.grid(row=2, column=1, sticky=(tk.NSEW))

        # definimos los encabezados que se muestran
        self.tabla.heading("lunes", text="Lunes")
        self.tabla.heading("martes", text="Martes")
        self.tabla.heading("miercoles", text="Miercoles")
        self.tabla.heading("jueves", text="Jueves")
        self.tabla.heading("viernes", text="Viernes")
    
    
        with open("eventos.csv", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            for fecha,hora,titulo,duracion,descripcion,importancia in lector:    # desempacamos las columnas en variables
                self.tabla.insert('', tk.END, values=(fecha,hora,titulo,duracion,descripcion)) # agregar datos al treeview

        # ejecutar callback cuando se seleccione (o des-seleccione) una fila
        self.tabla.bind('<<TreeviewSelect>>', self.item_seleccionado)

        # agregar barra de desplazamiento
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set) # la enlazamos al treeview
        scrollbar.grid(row=1, column=2, sticky=tk.NS)

        ttk.Button(self, text="Eliminar", command=self.eliminar).grid(row=10, column=1, columnspan=2, sticky=tk.S)
        ttk.Button(self, text="Nuevo", command=self.nuevo).grid(row=10, column=0, columnspan=2, sticky=tk.S)
    
    def item_seleccionado(self, event):
        # El evento se va a lanzar cuando se seleccione una fila y
        # cuando se deje de seleccionar una fila.
        print("Fila seleccionada o deseleccionada")
    
    def nuevo():
        toplevel = tk.Toplevel()
        toplevel.geometry("500x300")
        toplevel.resizable(False, False)
        ancho_pantalla = toplevel.winfo_screenwidth()     #Con este metodo calculamos el ancho de la pantalla
        altura_pantalla = toplevel.winfo_screenheight()   #Con este metodo calculamos el alto de la pantalla
        x_pos = int(ancho_pantalla / 2 - 800 / 2)
        y_pos = int(altura_pantalla / 2 - 600 / 2)
        toplevel.geometry("+{}+{}".format(x_pos, y_pos))
        Evento(toplevel).grid()
        
    def eliminar(self):
        seleccion = self.tabla.selection()
        # si selection() devuelve una tupla vacia, no hay seleccion
        if seleccion:
            for item_id in seleccion:
                item = self.tabla.item(item_id) # obtenemos el item y sus datos
                fila = item['values']
                res = askokcancel(title="Eliminar fila",
                                  message=("¿Desea eliminar esta fila?"
                                           "\n" + ",".join(fila)))
                if res:
                    self.tabla.delete(item_id)
        else:
            showinfo(message="Debe seleccionar una fila primero")

root = tk.Tk()
root.geometry("1200x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(400, 200)  # seteamos un tamaño minimo
root.title('Ejemplo de Treeview')
App(root).grid(sticky=tk.NSEW)
root.mainloop()