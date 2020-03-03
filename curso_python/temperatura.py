# -*- coding: utf-8 -*-

def promedio_temp(temps):
    suma_temps = 0

    for temp in temps:
        suma_temps += temp
    
    return suma_temps/len(temps)


if __name__ == '__main__':
    temps = []
    salir_ciclo = False
    while salir_ciclo == False:
        temps.append(float(input('ingrese temperatura: ')))
        if (input('desea agregar otra temperatura (s|n): ') == 'n'):
            salir_ciclo = True

    print(promedio_temp(temps))