import tkinter as tk
from tkinter import ttk
import datetime as dt


class Evento(ttk.Frame):
    """En esta clase evento voy a definir todos los atributos de un evento y voy a heredar los atributos
    de una clase superior, para eso heredo de Frame y con super()"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent= parent  # Hace referencia a la ventana principal
        parent.title("Esta es mi ventana para crear un evento")
        self.titulo = tk.StringVar()
        self.fecha_y_hora = tk.StringVar()
        self.duracion = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.importancia = tk.StringVar()


        #self.combo1_str = tk.StringVar()
        
        




        ttk.Label(self,text="Ingrese el titulo del evento", padding=3).grid(row=1, column=0)
        ttk.Entry(self,textvariable=self.titulo).grid(row=1, column=2) 

        ttk.Label(self,text="Fecha y hora del evento", padding=3).grid(row=2, column=0)
        ttk.Entry(self,textvariable=self.fecha_y_hora).grid(row=2, column=2)

        ttk.Label(self,text="Duración", padding=3).grid(row=3, column=0)
        ttk.Entry(self,textvariable=self.duracion).grid(row=3, column=2)

        ttk.Label(self,text="Descripción", padding=3).grid(row=4, column=0)
        ttk.Entry(self,textvariable=self.descripcion).grid(row=4, column=2) 
        
        ttk.Label(self,text="importancia", padding=3).grid(row=5, column=0)
        self.combo1 = ttk.Combobox(self, textvariable=self.importancia, width=17)
        self.combo1.grid(row=5, column=2, padx=5, pady=5)
        self.combo1["values"] = ("normal", "importante")
        self.combo1["state"] = "readonly"
        #self.combo1.bind('<<ComboboxSelected>>', self.on_combo_changed)





        #ttk.Entry(self,textvariable=self.importancia).grid(row=5, column=2)

        btn_guardar= ttk.Button(self, text="Guardar",command= self.guarda).grid(row=10, column=1)



    def guarda(self):
        import csv
        evento= self.titulo.get(), self.fecha_y_hora.get(), self.duracion.get(), self.descripcion.get(), self.importancia.get()
        with open("eventos.csv", "+a", newline="") as archivo:
            escritor = csv.writer(archivo, delimiter=",")
            escritor.writerow(evento)
        #self.parent.destroy()


"""Todas las lineas de abajo las tengo que comentar cuando eventos sea llamado de calendario.py"""
root = tk.Tk()
root.geometry("500x200")
Evento(root).grid()
root.resizable(False, False) # evita que se pueda cambiar de tamaño la ventana
root.mainloop()
