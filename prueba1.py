import csv
from datetime import datetime

# abrir el archivo CSV y cargar los datos en una lista de diccionarios
with open('eventos.csv', newline="") as archivo:
    lector = csv.DictReader(archivo)
    datos = [fila for fila in lector]
    
# función para extraer la fecha y hora de una fila y crear un objeto datetime
def clave_de_ordenamiento(fila):
    fecha = datetime.strptime(fila['fecha'], '%d/%m')
    hora = datetime.strptime(fila['hora'], '%H:%M')
    return datetime.combine(fecha.date(), hora.time())

# # ordenar la lista de datos por fecha y hora
datos_ordenados = sorted(datos, key=clave_de_ordenamiento)


# # nombres de las columnas en el archivo CSV
# columnas = ["fecha","hora","titulo","duracion","descripcion","importancia"]

# # abrir un archivo CSV para escribir los datos

# with open('evento2csv', 'w', newline='') as archivo:
#     escritor = csv.DictWriter(archivo, fieldnames=columnas)

#     # escribir la fila de encabezado con los nombres de las columnas
#     escritor.writeheader()

#     # escribir cada fila en el archivo CSV
#     for fila in datos_ordenados:
#         escritor.writerow(fila)

