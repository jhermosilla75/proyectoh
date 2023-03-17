import tkinter as tk 
from tkinter import ttk,messagebox
from evento import Evento

class Calendario(ttk.Frame):
    def __init__(self, parent):         
        super().__init__(parent) 
        self.parent=parent
        parent.title("Ventana Principal del Calendario")
        parent.geometry("800x600")
        ancho_pantalla = parent.winfo_screenwidth()     #Con este metodo calculamos el ancho de la pantalla
        altura_pantalla = parent.winfo_screenheight()   #Con este metodo calculamos el alto de la pantalla
        x_pos = int(ancho_pantalla / 2 - 800 / 2)
        y_pos = int(altura_pantalla / 2 - 600 / 2)
        parent.geometry("+{}+{}".format(x_pos, y_pos))  # Configura la posición de la ventana en la pantalla
        
        #creo los botones defino las acciones y los muestro
        #tengo que averiguar como posicionar los botones
        self.boton_nuevo=ttk.Button(self,text='Nuevo Evento',command=self.nuevo)
        self.boton_nuevo.grid(row=10, column=0)
        self.boton_nuevo.bind('<Return>',self.nuevo)
        self.boton_nuevo.bind('<Escape>',lambda event: self.parent.destroy())  # No se que hace esto, tengo que preguntar
        
        self.boton_editar=ttk.Button(self,text='Modificar Evento',command=self.editar)
        self.boton_editar.grid(row=11, column=0)
        self.boton_editar.bind('<Return>',self.editar)
        self.boton_editar.bind('<Escape>',lambda event: self.parent.destroy())  
        
        self.boton_elimina=ttk.Button(self,text='Elimina un Evento',command=self.elimina)
        self.boton_elimina.grid(row=12, column=0)
        self.boton_elimina.bind('<Return>',self.elimina)
        self.boton_elimina.bind('<Escape>',lambda event: self.parent.destroy())  # 
        
        #parent.grid_rowconfigure(0, weight=1)      #esto es para centrar los botones
        #parent.grid_columnconfigure(0, weight=1)   #esto es para centrar los botones


        
    def nuevo(self, event=None):
        root = tk.Tk()
        root.geometry("500x200")
        Evento(root).grid()
        root.resizable(False, False) # evita que se pueda cambiar de tamaño la ventana
        # toplevel = tk.Toplevel(self.parent)
        # Evento()
        


    def editar(self, event=None):
        print("Modifica un evento")

    def elimina(self, event=None):
        print("Elimina un evento")


root = tk.Tk() 
Calendario(root).grid()
root.mainloop() 