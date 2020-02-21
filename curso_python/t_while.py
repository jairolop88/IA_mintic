# -*- coding: utf-8 -*-
import random

def run():
    
    limite = int(raw_input('indicar un numero: '))
    encontrado = False
    numero_randon = random.randint(0,limite)

    while not encontrado:
        num = int(raw_input('adivina el numero: '))

        if num == numero_randon:
            print 'encontraste el numero'
            encontrado = True
        elif num < numero_randon:
            print 'el numero es mayor'
        elif num > numero_randon:
            print 'el numero es menor'


if __name__ == '__main__':
    run()