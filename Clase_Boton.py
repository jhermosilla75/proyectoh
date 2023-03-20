import tkinter as tk

import os
# Obtener la ruta absoluta del archivo actual (el script de Python).
abs_path = os.path.abspath(__file__)
# Obtener el directorio de la ruta del archivo.
dir_path = os.path.dirname(abs_path)
# Cambiar la carpeta de trabajo actual a la ubicación del archivo.
os.chdir(dir_path)

class Mi_Boton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.configure(bg="black", 
                       fg="#ffcc66", 
                       border=0, 
                       activeforeground="black", 
                       activebackground = "#ffcc66", 
                       width=15, 
                       height=2)
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
    
    def on_enter(self, event):
         self.config(bg="#ffcc66", fg="black")

    def on_leave(self, event):
         self.config(bg="black", fg="#ffcc66")

     

# Crear un botón de prueba
if __name__ == "__main__":
    ventana=tk.Tk()
    boton_prueba = Mi_Boton(ventana, text="Botón de prueba", command=lambda:print("Botón de prueba"))
    boton_prueba.grid()
    ventana.mainloop()