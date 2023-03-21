import tkinter as tk 
from tkinter import ttk,messagebox
import datetime as dt
from datetime import datetime
from tkcalendar import Calendar, DateEntry

from tkinter.messagebox import askokcancel, showinfo
import csv
import os


class Calendario(ttk.Frame):
    def __init__(self, parent):         
        super().__init__(parent) 
        self.parent=parent
        parent.title("Ventana Principal del Turnero")
        parent.geometry("1200x600")

        self.boton_nuevo=ttk.Button(self,text='Nuevo Evento',command=self.nuevo)
        self.boton_nuevo.grid(row=3, column=8)
        self.boton_nuevo.bind('<Return>',self.nuevo)
        self.boton_nuevo.bind('<Escape>',lambda event: self.parent.destroy())  # No se que hace esto, tengo que preguntar
        
        
        self.boton_editar=ttk.Button(self,text='Modificar Evento',command=self.editar)
        self.boton_editar.grid(row=3, column=9)
        self.boton_editar.bind('<Return>',self.editar)
        self.boton_editar.bind('<Escape>',lambda event: self.parent.destroy())  
        
        self.boton_eliminar=ttk.Button(self,text='Elimina un Evento',command=self.eliminar)
        self.boton_eliminar.grid(row=3, column=10)
        self.boton_eliminar.bind('<Return>',self.eliminar)
        self.boton_eliminar.bind('<Escape>',lambda event: self.parent.destroy())

        dia1= ttk.Label(self,text="LUNES", padding=3, width=20).grid(row=1, column=7)
        dia2= ttk.Label(self,text="MARTES", padding=3, width=20).grid(row=1, column=8)
        dia3= ttk.Label(self,text="MIERCOLES", padding=3, width=20).grid(row=1, column=9)
        dia4= ttk.Label(self,text="JUEVES", padding=3, width=20).grid(row=1, column=10)
        dia5= ttk.Label(self,text="VIERNES", padding=3, width=20).grid(row=1, column=11)

        self.grilla = ttk.Treeview(self, columns=("fecha","hora","titulo", "duracion", "descripcion", "importancia"), show='headings', selectmode="browse")

        # Define el encabezado de las columnas
        #treeview.heading("#0", text="ID")
        self.grilla.heading("fecha", text="Fecha")
        self.grilla.heading("hora", text="Hora")
        self.grilla.heading("titulo", text="Titulo")
        self.grilla.heading("duracion", text="Duracion")
        self.grilla.heading("descripcion", text="Descripcion")
        self.grilla.heading("importancia", text="Importancia")

        self.grilla.grid(row=2, column=7,columnspan=5, padx=10, pady= 100)  # , sticky=(tk.NSEW) averiguar que funcion cumple sticky
        self.carga_datos()
        
        # ejecutar callback cuando se seleccione (o des-seleccione) una fila
        #self.grilla.bind('<<TreeviewSelect>>', self.turno_seleccionado)

        # agregar barra de desplazamiento   (si tengo tiempo veo lo del scroll)
        # scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.grilla.yview)
        # self.grilla.configure(yscroll=scrollbar.set) # la enlazamos al treeview
        # scrollbar.grid(row=2, column=12, sticky=tk.NS)
    
    def turno_seleccionado(self, event):
        # El evento se va a lanzar cuando se seleccione una fila y
        # cuando se deje de seleccionar una fila.
        print("turno seleccionada o deseleccionada")
    
    
    def carga_datos(self):
        """ aqui va el doc"""
        self.grilla.delete(*self.grilla.get_children())
        with open("eventos.csv", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            encabezado = next(lector)
            for fecha,hora,titulo,duracion,descripcion, importancia in lector:    # desempacamos las columnas en variables
                self.grilla.insert('', tk.END, values=(fecha,hora,titulo,duracion,descripcion,importancia))


    def nuevo(self):
        """En esta funcion creo la ventana donde voy a cargar los nuevos turnos llamando a la clase Evento"""
        toplevel = tk.Toplevel(self.parent)
        toplevel.geometry("500x300")
        toplevel.resizable(False, False)
        ancho_pantalla = toplevel.winfo_screenwidth()     #Con este metodo calculamos el ancho de la pantalla
        altura_pantalla = toplevel.winfo_screenheight()   #Con este metodo calculamos el alto de la pantalla
        x_pos = int(ancho_pantalla / 2 - 800 / 2)
        y_pos = int(altura_pantalla / 2 - 600 / 2)
        toplevel.geometry("+{}+{}".format(x_pos, y_pos))
        toplevel.grab_set()
        Evento(toplevel, calendario_instance=self).grid()
        self.grilla.grid(row=2, column=7,columnspan=5, padx=10, pady= 100)  # , sticky=(tk.NSEW) averiguar que funcion cumple sticky
        

    def editar(self):
        pass

    def eliminar(self):
        seleccion = self.grilla.selection()
        # si selection() devuelve una tupla vacia, no hay seleccion
        if seleccion:
            for item_id in seleccion:
                item = self.grilla.item(item_id) # obtenemos el item y sus datos
                fila_borrar = list(item['values'])
                fila_borrar[3]= str(fila_borrar[3])
                res = askokcancel(title="Eliminar fila", message=("Esta seguro de eliminar el turno?"))
                if res:
                    self.grilla.delete(item_id)
                    #Abrir el archivo CSV y leerlo en una lista de listas
                    with open('eventos.csv', 'r') as archivo:
                        lector = csv.reader(archivo)
                        encabezado = next(lector)
                        filas = [fila for fila in lector]
                        for i in filas:
                           if i == fila_borrar:
                                print(i)
                                print("tengo que borrar esta fila y salir")
                                del(i)
                        print(filas)
                           
                    # columnas = ["fecha","hora","titulo","duracion","descripcion","importancia"]
                    # with open('eventos.csv', 'w', newline='') as archivo:
                    #     escritor = csv.DictWriter(archivo, fieldnames=columnas)
                    #     escritor.writeheader()
                    #     for fila in filas:
                    #         escritor.writerow(fila)

                else:
                    showinfo(message="Debe seleccionar una fila primero")
        

class Evento(ttk.Frame):
    """En esta clase Evento voy a definir todos los atributos de un evento en este caso son turnos 
    y voy a heredar los atributos de una clase superior, para eso heredo de Frame y con super()"""
    #def __init__(self, parent):
    def __init__(self, parent, calendario_instance=None):
        super().__init__(parent)
        self.parent= parent  # Hace referencia a la ventana principal
        self.calendario_instance=calendario_instance
        parent.title("Carga nuevo Turno")
        parent.geometry("600x300") 
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
        def chequear():
            if entradat.get() and entradaf.get() and entradah.get() and combo.get() and combo1.get():
                btn_guardar.config(state=tk.NORMAL)
            else:
                btn_guardar.config(state=tk.DISABLED)
        
        ttk.Label(self,text="Hora ", padding=3).grid(row=3, column=0)
        
        horas_atencion= [17,18,19,20,21]
        hora = [str(h).zfill(2) for h in horas_atencion]
        minuto = [str(m * 15).zfill(2) for m in range(4)]
        opciones = [h + ":" + m  for h in hora for m in minuto]
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
        
    def guarda(self):
        fecha = self.fecha.get()
        fecha_obj = datetime.strptime(fecha, '%d/%m/%y')
        dia = fecha_obj.day
        mes = fecha_obj.month
        anio = fecha_obj.year
        habiles= (1,2,3,6,7,8,9,10,13.14,15,16,17,20,21,22,23,24,27,28,29,30,31)
        fechaaguardar =str(dia)+"/"+str(mes)
        with open("eventos.csv", "r", newline="") as archivo:
            lector = csv.reader(archivo)
            #encabezado = next(lector)
            for i in lector:
                if fechaaguardar == i[0] and self.hora.get() == i[1]:
                    messagebox.showinfo(self, message="Ya existe un turno en esta fecha y horario")
                    return

        if mes != 3 or anio != 2023 or dia not in  habiles:
            messagebox.showwarning(message="Las fecha de los turnos debe ser un dia habil de Marzo de 2023")
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
            
        self.calendario_instance.carga_datos()
        self.parent.destroy()




root = tk.Tk() 
Calendario(root).grid()
root.resizable(tk.FALSE, tk.FALSE)
root.mainloop() 
