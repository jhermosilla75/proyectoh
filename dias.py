import tkinter as tk

# Creamos la ventana
ventana = tk.Tk()

# Añadimos un título a la ventana
ventana.title("Horario")

# Creamos un widget LabelFrame para los días de la semana
dias_label_frame = tk.LabelFrame(ventana, text="Días de la semana")

# Creamos los widgets Label para los días de la semana
lunes = tk.Label(dias_label_frame, text="Lunes")
martes = tk.Label(dias_label_frame, text="Martes")
miercoles = tk.Label(dias_label_frame, text="Miércoles")
jueves = tk.Label(dias_label_frame, text="Jueves")
viernes = tk.Label(dias_label_frame, text="Viernes")
sabado = tk.Label(dias_label_frame, text="Sábado")
domingo = tk.Label(dias_label_frame, text="Domingo")

# Añadimos los widgets Label al widget LabelFrame
lunes.grid(row=0, column=0)
martes.grid(row=0, column=1)
miercoles.grid(row=0, column=2)
jueves.grid(row=0, column=3)
viernes.grid(row=0, column=4)
sabado.grid(row=0, column=5)
domingo.grid(row=0, column=6)

# Añadimos el widget LabelFrame a la ventana
dias_label_frame.pack()

# Creamos un widget LabelFrame para el horario
horario_label_frame = tk.LabelFrame(ventana, text="Horario")

# Creamos los widgets Label para las horas del horario
hora_8 = tk.Label(horario_label_frame, text="8:00")
hora_9 = tk.Label(horario_label_frame, text="9:00")
hora_10 = tk.Label(horario_label_frame, text="10:00")
hora_11 = tk.Label(horario_label_frame, text="11:00")
hora_12 = tk.Label(horario_label_frame, text="12:00")
hora_13 = tk.Label(horario_label_frame, text="13:00")
hora_14 = tk.Label(horario_label_frame, text="14:00")
hora_15 = tk.Label(horario_label_frame, text="15:00")
hora_16 = tk.Label(horario_label_frame, text="16:00")
hora_17 = tk.Label(horario_label_frame, text="17:00")
hora_18 = tk.Label(horario_label_frame, text="18:00")

# Añadimos los widgets Label al widget LabelFrame
hora_8.grid(row=0, column=0)
hora_9.grid(row=1, column=0)
hora_10.grid(row=2, column=0)
hora_11.grid(row=3, column=0)
hora_12.grid(row=4, column=0)
hora_13.grid(row=5, column=0)
hora_14.grid(row=6, column=0)
hora_15.grid(row=7, column=0)
hora_16.grid(row=8, column=0)
hora_17.grid(row=9, column=0)
hora_18.grid(row=10, column=0)

# Añadimos el widget LabelFrame a la ventana
horario_label_frame.pack()

#
contenido_lunes_8 = tk.Label(horario_label_frame, text="Clase de matemáticas")
contenido_lunes_8.grid(row=0, column=1)

contenido_martes_8 = tk.Label(horario_label_frame, text="Clase de ciencias")
contenido_martes_8.grid(row=0, column=2)

contenido_miercoles_8 = tk.Label(horario_label_frame, text="Clase de historia")
contenido_miercoles_8.grid(row=0, column=3)

contenido_jueves_8 = tk.Label(horario_label_frame, text="Clase de literatura")
contenido_jueves_8.grid(row=0, column=4)

contenido_viernes_8 = tk.Label(horario_label_frame, text="Clase de arte")
contenido_viernes_8.grid(row=0, column=5)

horario_label_frame.pack()
ventana.mainloop()
