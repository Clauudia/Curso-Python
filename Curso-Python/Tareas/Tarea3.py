#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

from random import choice
import re

o = ('O','o','0','*','.')
a = ('A','a','4','#')
i = ('I','i','1','¡')
e = ('E','e','3', '?')
l = ('L','l','1','!')
s = ('S','s','5','$')
g = ('G','g','6','¿')
t = ('T','t','7','%')
b = ('B','b','8','&')
z = ('Z','z','2')
q = ('Q','q','9')
c = ('(', '[')

patrono = '[oO0]'
patrona = '[aA4]'
patroni = '[Ii1]'
patrone = '[eE3]'
patronl = '[Ll1]'
patrons = '[Ss5]'
patrong = '[Gg6]'
patront = '[Tt7]'
patronb = '[Bb8]'
patronz = '[Zz2]'
patronq = '[Qq9]'
patronc = '[Cc]'


def crea_contrasenas(archivo1, archivo2):
	with open(archivo1, 'r') as entrada, open(archivo2, 'w') as salida:
		for linea in entrada.readlines():		
			linea = linea.split(':')
			cadena = linea[1]
			for patrono in cadena:
				cadena = cadena.replace(patrono, choice(o))
				salida.write(cadena)
			for patrona in cadena:
				cadena = cadena.replace(patrona, choice(a))
				salida.write(cadena)
			for patroni in cadena:
				cadena = cadena.replace(patroni, choice(i))
				salida.write(cadena)
			for patrone in cadena:
				cadena = cadena.replace(patrone, choice(e))
				salida.write(cadena)
			for patronl in cadena:
				cadena = cadena.replace(patronl, choice(l))
				salida.write(cadena)
			for patrons in cadena:
				cadena = cadena.replace(patrons, choice(s))
				salida.write(cadena)
			for patrong in cadena:
				cadena = cadena.replace(patrong, choice(g))
				salida.write(cadena)
			for patront in cadena:
				cadena = cadena.replace(patront, choice(t))
				salida.write(cadena)
			for patronb in cadena:
				cadena = cadena.replace(patronb, choice(b))
				salida.write(cadena)
			for patronz in cadena:
				cadena = cadena.replace(patronz, choice(z))
				salida.write(cadena)
			for patronq in cadena:
				cadena = cadena.replace(patronq, choice(q))
				salida.write(cadena)
			for patronc in cadena:
				cadena = cadena.replace(patronc, choice(c))
				salida.write(cadena)

	entrada.close()
	salida.close()

crea_contrasenas('prueba.txt', 'contrasena.txt')