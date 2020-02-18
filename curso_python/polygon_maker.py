# -*- coding: utf-8 -*-

import turtle

def main():
	window = turtle.Screen()
	tortuga = turtle.Turtle()
	
	make_polygon(tortuga)

	turtle.mainloop()


def make_polygon(tortuga):
	length = int(raw_input('indica el largo de cada lado: '))
	lados = int(raw_input('indique el numero de lados que tendra el poligono: '))
	turn = 360.0/lados

	for i in range(lados):
		make_line_and_turn(tortuga, length, turn)

def make_line_and_turn(tortuga, length, turn):
	tortuga.forward(length)
	tortuga.left(turn)


if __name__ == '__main__':
	main()