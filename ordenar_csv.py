import csv

import csv

with open('eventos.csv') as archivo:
    lector = csv.reader(archivo)
    datos = list(lector)
ordenados = sorted(datos, key=lambda x: (x[0], x[1]))
for i in datos:
    print(i)
for i in ordenados:
    print(i)

# with open('archivo_ordenado.csv', mode='w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     for fila in ordenados:
#         writer.writerow(fila)

