import tkinter as tk
import tkinter.ttk as ttk

# Creamos una instancia de la ventana
ventana = tk.Tk()
ventana.title("Horario de clases")

# Creamos un widget Treeview con 6 columnas (lunes a viernes) y 9 filas (horas)
horario_tabla = ttk.Treeview(ventana, columns=("Lunes", "Martes", "Miércoles", "Jueves", "Viernes"))
horario_tabla.grid(row=0, column=0)

# Configuramos las columnas
horario_tabla.column("#0", width=100)
horario_tabla.column("Lunes", width=100)
horario_tabla.column("Martes", width=100)
horario_tabla.column("Miércoles", width=100)
horario_tabla.column("Jueves", width=100)
horario_tabla.column("Viernes", width=100)

# Añadimos los encabezados de las columnas
horario_tabla.heading("#0", text="Horas")
horario_tabla.heading("Lunes", text="Lunes")
horario_tabla.heading("Martes", text="Martes")
horario_tabla.heading("Miércoles", text="Miércoles")
horario_tabla.heading("Jueves", text="Jueves")
horario_tabla.heading("Viernes", text="Viernes")

# Añadimos las filas con los contenidos
horario_tabla.insert("", "end", text="8:00 - 9:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))
horario_tabla.insert("", "end", text="9:00 - 10:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))
horario_tabla.insert("", "end", text="10:00 - 11:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))
horario_tabla.insert("", "end", text="11:00 - 12:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))
horario_tabla.insert("", "end", text="12:00 - 13:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))
horario_tabla.insert("", "end", text="13:00 - 14:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))
horario_tabla.insert("", "end", text="14:00 - 15:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))

horario_tabla.insert("", "end", text="15:00 - 16:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))
horario_tabla.insert("", "end", text="16:00 - 17:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))
horario_tabla.insert("", "end", text="17:00 - 18:00", values=("Clase de matemáticas", "Clase de ciencias", "Clase de historia", "Clase de literatura", "Clase de arte"))

ventana.mainloop()
