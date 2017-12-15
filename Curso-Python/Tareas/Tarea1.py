#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def valida_palindromo(cadena):
	if cadena == cadena[::-1]:
		print "Es palíndromo"
	else:
		print "No es palíndromo"

