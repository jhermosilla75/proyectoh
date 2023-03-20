import tkinter as tk 
from tkinter import ttk,messagebox
from tkcalendar import DateEntry
from evento import Evento
from modifica import Modifica
import csv

class Calendario(ttk.Frame):
    def __init__(self, parent):         
        super().__init__(parent) 
        self.parent=parent
        parent.title("Ventana Principal del Turnero")
        parent.geometry("1200x600")
        # ancho_pantalla = parent.winfo_screenwidth()     #Con este metodo calculamos el ancho de la pantalla
        # altura_pantalla = parent.winfo_screenheight()   #Con este metodo calculamos el alto de la pantalla
        # x_pos = int(ancho_pantalla / 2 - 800 / 2)
        # y_pos = int(altura_pantalla / 2 - 600 / 2)
        # parent.geometry("+{}+{}".format(x_pos, y_pos))  # Configura la posición de la ventana en la pantalla
        
        #creo los botones defino las acciones y los muestro
        #tengo que averiguar como posicionar los botones
        self.boton_nuevo=ttk.Button(self,text='Nuevo Evento',command=self.nuevo)
        self.boton_nuevo.grid(row=3, column=8)
        self.boton_nuevo.bind('<Return>',self.nuevo)
        self.boton_nuevo.bind('<Escape>',lambda event: self.parent.destroy())  # No se que hace esto, tengo que preguntar
        
        self.boton_editar=ttk.Button(self,text='Modificar Evento',command=self.editar)
        self.boton_editar.grid(row=3, column=9)
        self.boton_editar.bind('<Return>',self.editar)
        self.boton_editar.bind('<Escape>',lambda event: self.parent.destroy())  
        
        self.boton_elimina=ttk.Button(self,text='Elimina un Evento',command=self.elimina)
        self.boton_elimina.grid(row=3, column=10)
        self.boton_elimina.bind('<Return>',self.elimina)
        self.boton_elimina.bind('<Escape>',lambda event: self.parent.destroy())
        dia1= ttk.Label(self,text="LUNES", padding=3, width=20).grid(row=1, column=7)
        dia2= ttk.Label(self,text="MARTES", padding=3, width=20).grid(row=1, column=8)
        dia3= ttk.Label(self,text="MIERCOLES", padding=3, width=20).grid(row=1, column=9)
        dia4= ttk.Label(self,text="JUEVES", padding=3, width=20).grid(row=1, column=10)
        dia5= ttk.Label(self,text="VIERNES", padding=3, width=20).grid(row=1, column=11)

        self.grilla = ttk.Treeview(self, columns=("fecha","hora","titulo", "duracion", "descripcion"), show='headings', selectmode="browse")

        # Define el encabezado de las columnas
        #treeview.heading("#0", text="ID")
        self.grilla.heading("fecha", text="Fecha")
        self.grilla.heading("hora", text="Hora")
        self.grilla.heading("titulo", text="Titulo")
        self.grilla.heading("duracion", text="Duracion")
        self.grilla.heading("descripcion", text="Descripcion")
        self.grilla.grid(row=2, column=7,columnspan=5, padx=10, pady= 100)  # , sticky=(tk.NSEW) averiguar que funcion cumple sticky
        self.carga_datos()
        


        #parent.grid_rowconfigure(0, weight=1)      #esto es para centrar los botones
        #parent.grid_columnconfigure(0, weight=1)   #esto es para centrar los botones

    def carga_datos(self):
        with open("eventos.csv", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            encabezado = next(lector)
            for fecha,hora,titulo,duracion,descripcion, importancia in lector:    # desempacamos las columnas en variables
                self.grilla.insert('', tk.END, values=(fecha,hora,titulo,duracion,descripcion))
        
    def nuevo(self):
        toplevel = tk.Toplevel(self.parent)
        toplevel.geometry("500x300")
        toplevel.resizable(False, False)
        ancho_pantalla = toplevel.winfo_screenwidth()     #Con este metodo calculamos el ancho de la pantalla
        altura_pantalla = toplevel.winfo_screenheight()   #Con este metodo calculamos el alto de la pantalla
        x_pos = int(ancho_pantalla / 2 - 800 / 2)
        y_pos = int(altura_pantalla / 2 - 600 / 2)
        toplevel.geometry("+{}+{}".format(x_pos, y_pos))
        toplevel.grab_set()
        Evento(toplevel).grid()
        self.grilla.delete('all')
        
        
        


    def editar(self, event=None):
        toplevel = tk.Toplevel(self.parent)
        toplevel.geometry("500x300")
        toplevel.resizable(False, False)
        ancho_pantalla = toplevel.winfo_screenwidth()     #Con este metodo calculamos el ancho de la pantalla
        altura_pantalla = toplevel.winfo_screenheight()   #Con este metodo calculamos el alto de la pantalla
        x_pos = int(ancho_pantalla / 2 - 800 / 2)
        y_pos = int(altura_pantalla / 2 - 600 / 2)
        toplevel.geometry("+{}+{}".format(x_pos, y_pos))
        Modifica(toplevel).grid()
        print("Modifica un evento")
        print("Modifica un evento")

    def elimina(self, event=None):
        print("Elimina un evento")


root = tk.Tk() 
Calendario(root).grid()
root.resizable(tk.FALSE, tk.FALSE)
root.mainloop() 