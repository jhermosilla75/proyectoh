def diames(dia, mes, anio):
    """ con esta formula determinamos en que día de la semana comienza el mes"""
    if mes in [1,2]:
        mes += 12
        anio -= 1
    q, m, y= dia, mes, anio
    h = q + ((13 *  (m+1)) //5) + y + (y//4) - (y // 100) + (y // 400) % 7
    return (h-1) % 7


def can_dias_mes(mes, anio):
    """Esta funcion sirve para determinar que cantidad de días tiene el mes"""
    if mes == 2:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            return 29
        else:
            return 28
    elif mes in [4, 6, 8, 10]:
        return 30
    else:
        return 31
    
def arma_calendario(mes, calendario):
    nombre_mes = {1:"ENERO", 2:"FEBRERO", 3:"MARZO", 4:"ABRIL", 5:"MAYO", 6:"JUNIO",
    7: "JULIO", 8:"AGOSTO", 9:"SETIEMBRE", 10:"OCTUBRE", 11:"NOVIEMBRE", 12:"DICIEMBRE"}
    print(nombre_mes[mes])
    print(" D  L  M  M  J  V  S")


# print(diames(1, 3, 2023))
# print(can_dias_mes(3, 2020))
arma_calendario(3, 2020)



