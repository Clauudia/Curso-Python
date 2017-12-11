#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

numero = input('ingresa el número de primos que quieres calcular: ' )
primos = [2]
contador = 1
n = 3

def calcula_primos(numero):
	if(numero < 1):
		print "Ingresa un entero mayor  0"
	else:
		while(contador <= numero):
			if(n % 2 != 0 and n % (n - 1) != 0):
				primos.append(n)
				contador + 1
				calcula_primos(numero + 2)
			else:
				calcula_primos(numero + 1)
print primos

