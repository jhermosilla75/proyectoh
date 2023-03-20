import tkinter as tk
from tkinter import ttk, messagebox
import datetime as dt
from datetime import datetime
from tkcalendar import Calendar, DateEntry
import os
import csv


class Evento(ttk.Frame):
    """En esta clase Evento voy a definir todos los atributos de un evento en este caso son turnos 
    y voy a heredar los atributos de una clase superior, para eso heredo de Frame y con super()"""
    def __init__(self, parent):
        super().__init__(parent)
        self.parent= parent  # Hace referencia a la ventana principal
        parent.title("Carga nuevo Turno")
        #parent.geometry("600x300") Esto lo define en calendario que es dedonde la llamo a esta clase
        self.titulo = tk.StringVar()
        self.fecha = tk.StringVar()
        self.hora = tk.StringVar()
        self.duracion = tk.StringVar()
        self.descripcion = tk.StringVar()
        self.importancia = tk.StringVar()

        ttk.Label(self,text="Nombre del paciente", padding=3).grid(row=1, column=0)
        entradat = ttk.Entry(self,textvariable=self.titulo)
        entradat.grid(row=1, column=2)
        entradat.bind("<KeyRelease>", lambda event: chequear())

        ttk.Label(self,text="Fecha ", padding=3).grid(row=2, column=0)
        entradaf= DateEntry(self, textvariable=self.fecha, width=8,  background="red", foreground="blue")
        entradaf.grid(row=2, column=2)
        entradaf.bind("<KeyRelease>", lambda event: chequear())
        
        ttk.Label(self,text="Hora ", padding=3).grid(row=3, column=0)
        
        horas_atencion= [17,18,19,20,21]
        hora = [str(h).zfill(2) for h in horas_atencion]
        minuto = [str(m * 15).zfill(2) for m in range(4)]
        opciones = [h + ":" + m  for h in hora for m in minuto]
        #ahora = dt.datetime.now().strftime("%H:%M")
        entradah = ttk.Combobox(self, textvariable=self.hora,  values= opciones, width=10)
        entradah.grid(row=3, column=2)
        entradah.set("17:00")
        entradah["state"] = "readonly"
                
        ttk.Label(self,text="Minutos de Duración", padding=3).grid(row=4, column=0)

        combo = ttk.Combobox(self, textvariable=self.duracion, values= ("15","30","45", "60"), width=10)
        combo.grid(row=4, column=2)
        combo.set("60")
        combo["state"] = "readonly"
                
        ttk.Label(self,text="Descripción", padding=3).grid(row=5, column=0)
        ttk.Entry(self,textvariable=self.descripcion).grid(row=5, column=2) 
        
        ttk.Label(self,text="importancia", padding=3).grid(row=6, column=0)
        combo1 = ttk.Combobox(self, textvariable=self.importancia, width=17)
        combo1.grid(row=6, column=2, padx=5, pady=5)
        combo1["values"] = ("normal", "importante")
        combo1["state"] = "readonly"
        combo1.set("normal")

        btn_guardar= ttk.Button(self, text="Guardar", state=tk.DISABLED, command= self.guarda)
        btn_guardar.grid(row=10, column=1)
        

        def chequear():
            if entradat.get() and entradaf.get() and entradah.get() and combo.get() and combo1.get():
                btn_guardar.config(state=tk.NORMAL)
            else:
                btn_guardar.config(state=tk.DISABLED)
        
    
    


    def guarda(self):
        fecha = self.fecha.get()
        fecha_obj = datetime.strptime(fecha, '%d/%m/%y')
        dia = fecha_obj.day
        mes = fecha_obj.month
        anio = fecha_obj.year
        fechaaguardar =str(dia)+"/"+str(mes)
        with open("eventos.csv", "r", newline="") as archivo:
            lector = csv.reader(archivo)
            #encabezado = next(lector)
            for i in lector:
                if fechaaguardar == i[0] and self.hora.get() == i[1]:
                    messagebox.showinfo(self, message="Ya existe un turno en esta fecha y horario")
                    return

        if mes != 3 or anio != 2023:
            messagebox.showwarning(message="Las fecha de los turnos deben ser de Marzo del 2023")
            return
        else:
            evento=  fechaaguardar, self.hora.get(), self.titulo.get(), self.duracion.get(), self.descripcion.get(), self.importancia.get()
            if os.path.exists("eventos.csv"):
                modoapertura = "+a"
            else:
                modoapertura = "w"
        with open("eventos.csv", modoapertura, newline="") as archivo:
            escritor = csv.writer(archivo, delimiter=",")
            escritor.writerow(evento)
            
        with open('eventos.csv', 'r') as archivo:
            lector = csv.DictReader(archivo)
            #encabezado = next(lector)
            datos = [fila for fila in lector]
            
        def clave_de_ordenamiento(fila):
            fecha = datetime.strptime(fila['fecha'], "%d/%m")
            hora = datetime.strptime(fila['hora'], '%H:%M')
            return datetime.combine(fecha.date(), hora.time()) 
        
        datos_ordenados = sorted(datos, key=clave_de_ordenamiento)


        columnas = ["fecha","hora","titulo","duracion","descripcion","importancia"]
        with open('eventos.csv', 'w', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)

            # escribir la fila de encabezado con los nombres de las columnas
            escritor.writeheader()
            # escribir cada fila en el archivo CSV
            for fila in datos_ordenados:
                escritor.writerow(fila)
            messagebox.showinfo(message="El turno se guardó con exito")
        
        



"""Todas las lineas de abajo las tengo que comentar cuando eventos sea llamado de calendario.py"""
# root = tk.Tk()
# root.geometry("500x200")
# Evento(root).grid()
# root.resizable(False, False) # evita que se pueda cambiar de tamaño la ventana
# root.mainloop()
