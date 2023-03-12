import datetime as dt

ahora = dt.datetime.now()

print(f"Fecha y Hora actual:  {ahora.day}  del  {ahora.month}  de  {ahora.year}  y son las {ahora.hour}:{ahora.minute}")

# con otro formato
ahora1 = ahora.strftime("%d/%m/%y")

print(f"la fecha actual es:  {ahora1}")