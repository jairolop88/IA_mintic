# -*- coding: utf-8 -*-

def run(palabra):
    print palabra == palabra[::-1]

if __name__ == '__main__':
    palabra = raw_input('indicar la palabra: ')
    run(palabra)