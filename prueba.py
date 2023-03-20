from datetime import datetime
import csv

fechaaguardar = "1/3"
hora= "17:00"
with open("eventos.csv", "r", newline="") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)
            cont = 1
            for i in lector:
                cont += 1
                print(fechaaguardar)
                print(i[0])
                print(hora)
                print(i[1])
                print(cont)
                if fechaaguardar == i[0] and hora == i[1]:
                     print("PASA POR AQUI EXISTE EL EVENTO")
                     break
                else:
                     print("NO EXISTE EL EVENTO")    
