# -*- coding: utf-8 -*-
# para escribir caracteres con tildes, al string que se vaya a escribir se debe anteponer la letra "u"

def run():

# para la version 3 de python el metodo raw_input(), paso a ser solamente input()

    nombre = raw_input('escribe tu nombre: ') #para version python 2
    edad = int(raw_input('escribe tu edad: ')) #para version python 2

    #nombre = input('escribe tu nombre: ') #para version python 3
    #edad = int(input('escribe tu edad: ')) #para version python 3

    
    print(u'me llamo {} y tengo {} años'.format(nombre,edad)) #para version python 2
    #print('me llamo {} y tengo {} años'.format(nombre,edad)) #para version python 3


if __name__ == '__main__':
    run()