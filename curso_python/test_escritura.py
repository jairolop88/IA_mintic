# -*- coding: utf-8 -*-

def run():

    nombre = raw_input('escribe tu nombre: ')
    edad = int(raw_input('escribe tu edad: '))

    print(u'me llamo ${} y tengo ${} años'.format(nombre,edad))


if __name__ == '__main__':
    run()