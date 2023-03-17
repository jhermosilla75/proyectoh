import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()
root.geometry("300x200")

# Crear una variable de cadena para almacenar la fecha seleccionada
selected_date = tk.StringVar()

# Crear un widget de fecha utilizando el widget DateEntry de tkcalendar
date_picker = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')

# Enlazar la variable de cadena a la fecha seleccionada en el widget
date_picker.config(date_pattern='yyyy-mm-dd', textvariable=selected_date)

# Agregar el widget a la ventana
date_picker.pack(padx=10, pady=10)

root.mainloop()
