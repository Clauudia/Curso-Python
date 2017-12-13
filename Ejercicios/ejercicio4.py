#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
from poo1 import Becario

#calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

calificacionesL = []

#def asigna_calificaciones():
#    for b in becarios:
#        calificacion_alumno[b] = choice(calificaciones)

#def imprime_calificaciones():
#    for alumno in calificacionesL:
#        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def crea_lista():
    for alumno in calificacion_alumno:
        calificacionesL.append(Becario(alumno, choice(calificaciones)))
    return calificacionesL

#asigna_calificaciones()
#imprime_calificaciones()
crea_lista()
