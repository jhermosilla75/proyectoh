import tkinter as tk 
from tkinter import ttk,messagebox
import datetime as dt
from datetime import datetime, timedelta
from datetime import date
from tkcalendar import Calendar, DateEntry

from tkinter.messagebox import askokcancel, showinfo
import csv
import os

class Calendario(ttk.Frame):
    def __init__(self, parent):         
        super().__init__(parent) 
        self.parent=parent
        parent.title("Turnero Marzo 2023")
        parent.geometry("1000x600")
        #self.recordatorio_un_dia_antes() 
        ancho_pantalla = parent.winfo_screenwidth()     #Con este metodo calculamos el ancho de la pantalla
        altura_pantalla =parent.winfo_screenheight()   #Con este metodo calculamos el alto de la pantalla
        x_pos = int(ancho_pantalla / 2 - 1000 / 2)
        y_pos = int(altura_pantalla / 2 - 600 / 2)
        parent.geometry("+{}+{}".format(x_pos, y_pos))
        parent.resizable(tk.FALSE, tk.FALSE)
        self.buca_paciente = tk.StringVar()
        self.buca_descripcion = tk.StringVar()
        self.buca_etiqueta = tk.StringVar()
        self.misemana =[]
        self.i = 0
        self.bandera = 0
        self.semana = False
        self.boton_nuevo=ttk.Button(self,text='Nuevo Turno',command=self.nuevo)
        self.boton_nuevo.grid(row=4, column=8)
        #self.boton_nuevo.bind('<Return>',self.nuevo)
        #self.boton_nuevo.bind('<Escape>',lambda event: self.parent.destroy())  
        
        self.boton_editar=ttk.Button(self,text='Modificar Turno',command=self.editar)
        self.boton_editar.grid(row=4, column=9)
        #self.boton_editar.bind('<Return>',self.editar)
        #self.boton_editar.bind('<Escape>',lambda event: self.parent.destroy())  
        
        self.boton_eliminar=ttk.Button(self,text='Eliminar Turno',command=self.eliminar)
        self.boton_eliminar.grid(row=4, column=10)
        #self.boton_eliminar.bind('<Return>',self.eliminar)
        #self.boton_eliminar.bind('<Escape>',lambda event: self.parent.destroy())

        self.boton_anterior=ttk.Button(self,text='Anterior semana',command=self.anterior)
        self.boton_anterior.grid(row=1, column=12)
        
        self.boton_siguiente=ttk.Button(self,text='siguiente semana',command=self.siguiente)
        self.boton_siguiente.grid(row=1, column=13)

        self.boton_semanal=ttk.Button(self,text='Vista Semanal', width= 15,command=self.semanal)
        self.boton_semanal.grid(row=2, column=12)

        self.boton_mensual=ttk.Button(self,text='Vista Mensual', width= 15,command=self.mensual)
        self.boton_mensual.grid(row=2, column=13)


        #Aqui voy a desarrollar la busqueda por paciente o por descripción
        self.label_busqueda = ttk.Label(self, text="BUSQUEDA", padding=3, width=20, font=('Bookman Old Style', 16, 'bold'), foreground='#FF0000')
        self.label_busqueda.grid(row=17, column=7, columnspan=5)
        
        ttk.Label(self,text="Buscar por paciente", padding=3, font=('Bookman Old Style', 11, 'bold')).grid(row=18, column=7)
        self.entradap= ttk.Entry(self,textvariable=self.buca_paciente)
        self.entradap.grid(row=18, column=8)
        self.entradap.bind("<KeyRelease>", lambda event: self.buscap("paciente"))

        ttk.Label(self,text="Buscar por Descripcion", padding=3, font=('Bookman Old Style', 11, 'bold')).grid(row=19, column=7)
        self.entradad= ttk.Entry(self,textvariable=self.buca_descripcion)
        self.entradad.grid(row=19, column=8)
        self.entradad.bind("<KeyRelease>", lambda event: self.buscap("descripcion"))

        ttk.Label(self,text="Buscar por Etiqueta", padding=3, font=('Bookman Old Style', 11, 'bold')).grid(row=20, column=7)
        self.entradae= ttk.Entry(self,textvariable=self.buca_etiqueta)
        self.entradae.grid(row=20, column=8)
        self.entradae.bind("<KeyRelease>", lambda event: self.buscap("etiqueta"))



        dia1= ttk.Label(self,text="LUNES", padding=3, width=20).grid(row=1, column=7)
        dia2= ttk.Label(self,text="MARTES", padding=3, width=20).grid(row=1, column=8)
        dia3= ttk.Label(self,text="MIERCOLES", padding=3, width=20).grid(row=1, column=9)
        dia4= ttk.Label(self,text="JUEVES", padding=3, width=20).grid(row=1, column=10)
        dia5= ttk.Label(self,text="VIERNES", padding=3, width=20).grid(row=1, column=11)

        self.semanas =  [(" ", " ", "1", "2", "3"), ("6", "7", "8", "9", "10"), 
                    ("13", "14", "15", "16", "17"), ("20", "21", "22", "23", "24"),
                    ("27", "28", "29", "30", "31")]
               
        self.grilla = ttk.Treeview(self, columns=("fecha","hora","paciente", "duracion", "descripcion", "importancia", "etiqueta", "recordatorio"), show='headings', selectmode="browse")
        self.grilla.config(height=15)
        style = ttk.Style()
        style.configure("Treeview.Heading", background="wheat4", foreground='red')
        
        # Define el encabezado de las columnas
        self.grilla.heading("fecha", text="Fecha", anchor=tk.CENTER)
        self.grilla.heading("hora", text="Hora", anchor=tk.CENTER)
        self.grilla.heading("paciente", text="Paciente", anchor=tk.CENTER)
        self.grilla.heading("duracion", text="Duracion", anchor=tk.CENTER)
        self.grilla.heading("descripcion", text="Descripcion", anchor=tk.CENTER)
        self.grilla.heading("importancia", text="Importancia")
        self.grilla.heading("etiqueta", text="Etiqueta")
        self.grilla.heading("recordatorio", text="Rec")
        self.grilla.column("fecha", width=70)
        self.grilla.column("hora", width=35)
        self.grilla.column("paciente", width=120)
        self.grilla.column("duracion", width=50)
        self.grilla.column("descripcion", width=180)
        self.grilla.column("importancia", width=50)
        self.grilla.column("etiqueta", width=100)
        self.grilla.column("recordatorio", width=0)
        

        self.pregunto_existe()
        """ aqui creo la grilla y llamo a la funcion/metodo carga_datos que carga la grilla segun corresponda"""
        self.grilla.grid(row=3, column=7,columnspan=5, padx=(10,10), pady= 10)
        self.carga_datos()
        """Controlo que los botones de siguiente y anterior semana esta habilitados o no según corresponda"""
        if self.i == 0:
            self.boton_anterior.config(state=tk.DISABLED)
        if self.i == 4:
            self.boton_siguiente.config(state=tk.DISABLED)
        self.boton_semanal.config(state=tk.DISABLED)
        self.dibuja_dias()
        
    
    def dibuja_dias(self):
        """En esta funcion dibujo los dias a mostrar en la vista semanal, se ejecuta cada vez que accionamos el
        boton anterior y siguiente semana"""
        ndia1= ttk.Label(self,text=self.misemana[0], padding=3, width=20).grid(row=2, column=7)
        ndia2= ttk.Label(self,text=self.misemana[1], padding=3, width=20).grid(row=2, column=8)
        ndia3= ttk.Label(self,text=self.misemana[2], padding=3, width=20).grid(row=2, column=9)
        ndia4= ttk.Label(self,text=self.misemana[3], padding=3, width=20).grid(row=2, column=10)
        ndia5= ttk.Label(self,text=self.misemana[4], padding=3, width=20).grid(row=2, column= 11)

    
    def pregunto_existe(self):
        if not os.path.exists("eventos.csv") or (os.path.exists("eventos.csv") and os.stat("eventos.csv").st_size == 0):
            columnas = ["fecha","hora","titulo","duracion","descripcion","importancia", "etiqueta", "recordatorio"]
            with open("eventos.csv", 'w', newline='') as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=columnas)
                escritor.writeheader()        
    
    def anterior(self):
        """Esta función se ejecuta cada vez que accionamos el boton anterior semana, basicamente lo que hace
        es habilitar y desabhilitar botones segun corresponda y setear bandera y semana para cargar la grilla
        con los datos que correspondan"""
        self.bandera = 1
        self.semana = True
        self.i -=1
        self.misemana= self.semanas[self.i]
        self.boton_siguiente.config(state=tk.NORMAL)
        if self.i == 0:
            self.boton_anterior.config(state=tk.DISABLED)
        for col in range(7, 12):
            self.grid_slaves(row=2, column=col)[0].grid_forget()
        self.dibuja_dias()
        return self.carga_datos()
    
    def siguiente(self):
        """Esta función se ejecuta cada vez que accionamos el boton siguiente semana, basicamente lo que hace
        es habilitar y desabhilitar botones segun corresponda y setear bandera y semana para cargar la grilla
        con los datos que correspondan"""
        self.bandera = 1
        self.semana = True
        self.i +=1
        self.misemana= self.semanas[self.i]
        self.boton_anterior.config(state=tk.NORMAL)
        if self.i == 4:
            self.boton_siguiente.config(state=tk.DISABLED)
        self.boton_semanal.config(state=tk.DISABLED)
        for col in range(7, 12):
            self.grid_slaves(row=2, column=col)[0].grid_forget()
        self.dibuja_dias()
        return self.carga_datos()
        
    def mensual(self):
        """Esta función se ejecuta cada vez que accionamos el boton Mensual, basicamente lo que hace
        es habilitar y desabhilitar botones segun corresponda y setear bandera y semana para cargar la grilla
        con los datos que correspondan"""
        self.semana = False
        self.bandera = 1
        self.boton_semanal.config(state=tk.NORMAL)
        self.boton_mensual.config(state=tk.DISABLED)
        self.boton_anterior.config(state=tk.DISABLED)
        self.boton_siguiente.config(state=tk.DISABLED)
        self.entradap.delete(0, "end")
        self.entradad.delete(0, "end")
        self.entradae.delete(0, "end")
        self.entradap.state(['!disabled'])
        self.entradad.state(['!disabled'])
        self.entradae.state(['!disabled'])
        for col in range(7, 12):
            self.grid_slaves(row=2, column=col)[0].grid_forget()
        ttk.Label(self, text="VISTA MENSUAL", padding=3, width=20).grid(row=2, column=7, columnspan=5)
        return self.carga_datos()

    def semanal(self):
        """Aqui basicamente controlo que botonones habilitar y sehabilitar segun corresponda 
        dibujo los días y cargamos la grilla con los nuevos datos"""
        self.semana = True
        self.bandera = 0
        self.boton_mensual.config(state=tk.NORMAL)
        self.boton_semanal.config(state=tk.DISABLED)
        self.boton_anterior.config(state=tk.NORMAL)
        self.boton_siguiente.config(state=tk.NORMAL)
        self.entradap.delete(0, "end")
        self.entradad.delete(0, "end")
        self.entradae.delete(0, "end")
        self.entradap.state(['!disabled'])
        self.entradad.state(['!disabled'])
        self.entradae.state(['!disabled'])
        if self.i == 0:
            self.boton_anterior.config(state=tk.DISABLED)
        if self.i == 4:
            self.boton_siguiente.config(state=tk.DISABLED)
        self.boton_semanal.config(state=tk.DISABLED)
        self.dibuja_dias()
        return self.carga_datos()

    def carga_datos(self):
        """ En esta funcion vamos a realizar la carga de la grilla necesitamos esta funcion ya que la vamos a llamar
        al iniciar el programa y despues que creemos un nuevo turno o modificamos un turno y cada vez que 
        accionemos los botones de semana mes, anterior o siguiente"""
        self.grilla.delete(*self.grilla.get_children())
        if self.bandera == 0:
            hoy = date.today()
            ddh= str(hoy.day)
            self.misemana =[]
            if ddh == "4" or  ddh == "5":
                messagebox.showinfo(message="Pasa por aqui")
                ddh = "6"
            elif ddh == "11" or ddh == "12":
                ddh = "13"
            elif ddh == "18" or ddh == "19":
                ddh = "20"
            elif ddh == "25" or ddh == "26":
                ddh = "27"
                        
            for i, tupla in enumerate(self.semanas):
                if ddh in tupla:
                    self.misemana=self.semanas[i]
                    self.i = i
                    self.semana = True
                    break
        
        with open("eventos.csv", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            encabezado = next(lector)
            for fecha,hora,paciente,duracion,descripcion, importancia, etiqueta, recordatorio in lector:    # desempacamos las columnas en variables
                if self.semana:
                    fechad = fecha[:-5] 
                    if fechad in self.misemana:
                        self.grilla.insert('', tk.END, values=(fecha,hora,paciente,duracion,descripcion,importancia, etiqueta, recordatorio))
                else:
                    
                    self.grilla.insert('', tk.END, values=(fecha,hora,paciente,duracion,descripcion,importancia, etiqueta, recordatorio))
                    # Recorrer todas las filas del TreeView y agregar etiqueta a las filas con Importancia = "Importante"
            for row_id in self.grilla.get_children():
                if self.grilla.item(row_id)["values"][5] == "importante":
                    self.grilla.item(row_id, tags=("importante",))
                    # Configurar estilo de la etiqueta "importante"
                    self.grilla.tag_configure("importante", background="LemonChiffon3", foreground="black")
                    
    
    def buscap(self,busqueda):
        """En esta función voy a realizar las busqueda ya sea por paciente, por descripción o por etiqueta, carga 
        en la grilla segun el criterio seleccionado y habilita y deshabilita los botones segun corresponda"""
        self.boton_siguiente.config(state=tk.DISABLED)
        self.boton_anterior.config(state=tk.DISABLED)
        self.boton_semanal.config(state=tk.NORMAL)
        self.boton_mensual.config(state=tk.NORMAL)

        if busqueda == "paciente":
            self.entradad.state(['disabled'])
            self.entradae.state(['disabled'])
            buscar = self.buca_paciente.get()
        elif busqueda == "descripcion":
            self.entradap.state(['disabled'])
            self.entradae.state(['disabled'])
            buscar = self.buca_descripcion.get()
        else:
            self.entradap.state(['disabled'])
            self.entradad.state(['disabled'])
            buscar = self.buca_etiqueta.get()
        if buscar:
            self.grilla.delete(*self.grilla.get_children())
            with open('eventos.csv') as archivo:
                lector = csv.reader(archivo, delimiter=',')
                encabezado = next(lector)
                for fecha,hora,paciente,duracion,descripcion, importancia, etiqueta, recordatorio in lector:
                    if busqueda == "paciente":
                        buscado = paciente
                    elif busqueda == "descripcion":
                        buscado = descripcion
                    else:
                        buscado = etiqueta
                    
                    if buscar.lower() in buscado.lower():
                        self.grilla.insert('', tk.END, values=(fecha,hora,paciente,duracion,descripcion,importancia, etiqueta, recordatorio))
                for row_id in self.grilla.get_children():
                    if self.grilla.item(row_id)["values"][5] == "importante":
                        self.grilla.item(row_id, tags=("importante",))
                        # Configurar estilo de la etiqueta "importante"
                        self.grilla.tag_configure("importante", background="LemonChiffon3", foreground="black")

        else:
            if busqueda == "paciente":
                self.entradad.state(['!disabled'])
                self.entradae.state(['!disabled'])
            elif busqueda == "descripcion":
                self.entradap.state(['!disabled'])
                self.entradae.state(['!disabled'])
            else:
                self.entradap.state(['!disabled'])
                self.entradad.state(['!disabled'])

            self.semanal()
    
    def nuevo(self, fila_editar= {}):
        """En esta funcion creo la ventana donde voy a cargar los nuevos turnos llamando a la clase Evento
        esta función tambien es llamada para modificar los turnos"""
        toplevel = tk.Toplevel(self.parent, fila_editar= None)
        self.fila_editar = fila_editar
        toplevel.geometry("500x400+300+200")
        toplevel.grab_set()
        Evento(toplevel, self.fila_editar, calendario_instance=self).grid()

    def editar(self):
        """En la funcion Editar voy a capturar los datos de la selección de la grilla y voy a mandar como
        argumento los datos a la funcion nuevo que usamos para dar de alta los turnos pero esta vez pasando los datos de la grilla"""
        seleccion = self.grilla.selection()
        if seleccion:
            for item_id in seleccion:
                item = self.grilla.item(item_id) # obtenemos el item y sus datos
                fila_editar = list(item['values'])
                self.nuevo(fila_editar)
        else:
            showinfo(message="Debe seleccionar una fila primero")

    def eliminar(self):
        """La funcion Eliminar captura los datos del turno seleccionado de la grilla y lo elimina 
        tanto de la grilla como del archivo csv"""
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
                                filas.remove(fila_borrar)
                                break
                        columnas = ["fecha","hora","paciente","duracion","descripcion","importancia", "etiqueta", "recordatorio"]
                        with open('eventos.csv', 'w', newline='') as archivo:
                            escritor = csv.writer(archivo, delimiter=",")
                            escritor.writerow(columnas)
                            for fila in filas:
                                escritor.writerow(fila)
                        messagebox.showinfo(message="El turno se elimino con exito")
        else:
            showinfo(message="Debe seleccionar una fila primero")
        
    # def recordatorio_un_dia_antes(self):
    #     hoy = datetime.now().date()
    #     with open("eventos.csv", 'r') as archivo:
    #         lector = csv.reader(archivo)
    #         next(lector)  
    #         for fila in lector:
    #             filas =[]
    #             fecha_hora = datetime.strptime(fila[0], '%d/%m/%y').date()
    #             if fecha_hora - hoy == timedelta(days=1):
    #                 messagebox.showinfo(self, message='Tiene turno mañana: {} - {}'.format(fila[2], fila[4]))
    #                 fila[7] = "False"
    #                 print(fila)
    #             filas.append(fila)
    #             print(filas)
            
        # columnas = ["fecha","hora","paciente","duracion","descripcion","importancia", "etiqueta", "recordatorio"]
        # with open("eventos.csv", 'w', newline='') as archivo:
        #     escritor = csv.DictWriter(archivo, fieldnames=columnas)
        #     escritor.writeheader()
        #     for fila in filas:
        #         escritor.writerow(fila)


class Evento(ttk.Frame):
    """En esta clase Evento voy a definir todos los atributos de un evento en este caso son turnos 
    y voy a heredar los atributos de una clase superior, para eso heredo de Frame y con super()"""
    def __init__(self, parent, fila_editar = {}, calendario_instance= None):
        super().__init__(parent)
        self.parent= parent  # Hace referencia a la ventana principal
        self.calendario_instance=calendario_instance
        self.fila_editar = fila_editar
        if fila_editar != {}:
            parent.title("Modifica Turno")
            self.control = True
        else:
            self.parent.title("Carga nuevo Turno")
            self.control = False
        self.titulo = tk.StringVar()
        self.fecha = DateEntry()
        self.hora = tk.StringVar()
        self.duracion = tk.StringVar()
        self.descripcion = tk.Text(height=4, width=20)
        self.importancia = tk.StringVar()
        self.etiqueta = tk.StringVar()
        self.var = tk.BooleanVar()

        if self.control:  # Si es modificacion de turno seteo los campos que capturé de la grilla
            fechat = fila_editar[0]
            fechat1 = datetime.strptime(fechat, '%d/%m/%y').date()
            self.titulo.set(fila_editar[2])
            self.hora.set(fila_editar[1])
            self.duracion.set(fila_editar[3])
            self.importancia.set(fila_editar[5])
            self.etiqueta.set(fila_editar[6])
            
        ttk.Label(self,text="Nombre del paciente", padding=3).grid(row=1, column=0)
        entradat = ttk.Entry(self,textvariable=self.titulo)
        entradat.grid(row=1, column=2)
        entradat.bind("<KeyRelease>", lambda event: chequear())
        
        ttk.Label(self,text="Fecha ", padding=3).grid(row=2, column=0)
        self.fecha= DateEntry(self)
        if self.control:
            self.fecha.set_date(fechat1)
        self.fecha.grid(row=2, column=2)
        self.fecha.bind("<KeyRelease>", lambda event: chequear())
        self.fecha["state"] = "readonly"
        def chequear():
            """Aqui controlo que los campos esten completos para habiliotar el boton guardar aunque en realidad
            lo unico que controla es el campo paciente, a los otros los tengo seteado con algo por defecto"""
            if entradat.get(): # and self.fecha.get() and entradah.get() and combo.get() and combo1.get():
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
        if self.control == False:
            entradah.set("17:00")
        entradah["state"] = "readonly"
                
        ttk.Label(self,text="Minutos de Duración", padding=3).grid(row=4, column=0)

        combo = ttk.Combobox(self, textvariable=self.duracion, values= ("15","30","45", "60"), width=10)
        combo.grid(row=4, column=2)
        if self.control == False:
            combo.set("60")
        combo["state"] = "readonly"
                
        ttk.Label(self,text="Descripción", padding=3).grid(row=5, column=0)
        self.descripcion = tk.Text(self, height=4, width=20)
        self.descripcion.grid(row=5, column=2) 
        if self.control:
            self.descripcion.insert(tk.END, fila_editar[4])
        ttk.Label(self,text="importancia", padding=3).grid(row=6, column=0)
        combo1 = ttk.Combobox(self, textvariable=self.importancia, width=17)
        combo1.grid(row=6, column=2, padx=5, pady=5)
        combo1["values"] = ("normal", "importante")
        combo1["state"] = "readonly"

        ttk.Label(self,text="Etiqueta", padding=3).grid(row=7, column=0)
        entradae = ttk.Entry(self,textvariable=self.etiqueta)
        entradae.grid(row=7, column=2)
        
        ttk.Label(self,text="Recordar el día anterior?", padding=20).grid(row=8, column=0)

        self.radio_si = tk.Radiobutton(self, text="Sí", variable=self.var, value=True)
        self.radio_si.grid(row=8, column=1, padx=1, pady=1)
        self.radio_no = tk.Radiobutton(self, text="No", variable=self.var, value=False)
        self.radio_no.grid(row=8, column=2, padx=1, pady=1)
        

        if self.control == False:
            combo1.set("normal")

        btn_guardar= ttk.Button(self, text="Guardar", state=tk.DISABLED, command= self.guarda)
        btn_guardar.grid(row=12, column=1)
        if self.control:
            btn_guardar.config(state=tk.NORMAL)
        
        btn_cancelar= ttk.Button(self, text="Cancelar", state=tk.NORMAL, command=self.parent.destroy)
        btn_cancelar.grid(row=12, column=4)

    def guarda(self):
        """Esta funcion se ejecuta cuando confirmamos la carga del turno con el boton guardar se usa tanto en la alta 
        de los turnos como en las modificaciones de los mismos"""
        habiles= (1,2,3,6,7,8,9,10,13,14,15,16,17,20,21,22,23,24,27,28,29,30,31)
        formato_str = "%d/%m/%y"
        fecha1 = datetime.strptime(self.fecha.get(), formato_str).date()
        dia = fecha1.day    
        mes= fecha1.month
        anio= 2023
        self.descripcion.get("1.0", "end-1c")
        if mes != 3 or anio != 2023 or dia not in  habiles:
            messagebox.showwarning(message="Las fecha de los turnos debe ser un dia habil de Marzo de 2023")
            return
        if self.control:
            self.fila_editar[3]= str(self.fila_editar[3])
        evento=  self.fecha.get(), self.hora.get(), self.titulo.get(), self.duracion.get(), self.descripcion.get("1.0", "end-1c"),self.importancia.get(), self.etiqueta.get(), self.var.get()
        with open("eventos.csv", "r", newline="") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)
            filas = [fila for fila in lector]
            for i in filas:
                if  self.fecha.get() == i[0] and self.hora.get() == i[1]:
                    if self.control == False:
                        messagebox.showinfo(self, message="Ya existe un turno en esta fecha y horario")
                        return
                    else:
                        if  self.fecha.get() != self.fila_editar[0] or self.hora.get() != self.fila_editar[1]:
                            messagebox.showinfo(self, message="Ya existe un turno en esta fecha y horario")
                            return
            for i in filas:
                if i == self.fila_editar:
                    filas.remove(self.fila_editar)
                    break
        filas.append(evento)
        with open("eventos.csv", "a+", newline="") as archivo:
            escritor = csv.writer(archivo, delimiter=",")
            for i in filas:
                escritor.writerow(i)
        columnas = ["fecha","hora","paciente","duracion","descripcion","importancia", "etiqueta", "recordatorio"]
        with open('eventos.csv', 'w', newline='') as archivo:
            escritor = csv.writer(archivo)
            # escribir la fila de encabezado con los nombres de las columnas
            escritor.writerow(columnas)
            # escribir cada fila en el archivo CSV
            for fila in filas:
                    escritor.writerow(fila)
        if self.control:
            messagebox.showinfo(message="El turno se modificó con exito")
        else:
            messagebox.showinfo(message="El turno se guardó con exito")
    
        with open('eventos.csv') as archivo:
            lector = csv.DictReader(archivo)
            lista_datos = [fila for fila in lector]
        def ordenar_por_fecha_hora(datos):
            def convertir_fecha_hora(fila):
                fecha_hora_str = fila['fecha'] + ' ' + fila['hora']
                return datetime.strptime(fecha_hora_str, '%d/%m/%y %H:%M')
            return sorted(datos, key=convertir_fecha_hora)
        lista_ordenada = ordenar_por_fecha_hora(lista_datos)
        columnas = ["fecha","hora","paciente","duracion","descripcion","importancia", "etiqueta", "recordatorio"]
        with open("eventos.csv", 'w', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            for fila in lista_ordenada:
                escritor.writerow(fila)
            
        self.calendario_instance.carga_datos()
        self.parent.destroy()

root = tk.Tk() 
Calendario(root).grid()
root.resizable(tk.FALSE, tk.FALSE)
root.mainloop() 

