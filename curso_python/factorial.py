# -*- coding:utf-8 -*-


def factorial(num):
    resultado = num
    for x in range(num):
        if x < num-1:
            resultado *= num - 1 - x
            print(resultado)

    return resultado

if __name__ == '__main__':  
    num = int(raw_input('indicar numero: '))
    print(factorial(num))