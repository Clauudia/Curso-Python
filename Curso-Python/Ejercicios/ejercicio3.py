#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

calificacion_alumno = {}
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
aprobados = []
reprobados = []

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def separa_aprobados_reprobados():
    for alumno in calificacion_alumno:
        if(calificacion_alumno[alumno] > 7):
            aprobados.append(alumno)                       
        else:
            reprobados.append(alumno)
    return tuple(reprobados), tuple (aprobados)
    #print 'los alumnos aprobados son: ' % aprobados 
    #print 'los alumnos reprobados son: ' % reprobados

def calcula_promedio():
    suma = 0
    for alumno in calificacion_alumno:
        suma += calificacion_alumno[alumno]
        promedio = float(suma) / 15.0
        #print 'El promedio es: ' % promedio
    return promedio

def conjunto_califs():
    calificaciones = []
    for alumno in calificaciones_alumno:
        calificaciones.append(calificacion_alumno[alumno])
    return calificaciones


asigna_calificaciones()
imprime_calificaciones()
separa_aprobados_reprobados()
calcula_promedio()

#print 'Los alumnos aprobados son: ' % aprobados
#print 'Los alumnos reprobados son: ' % reprobados
#print 'El promedio del grupo es : ' % promedio
#print 'las calificaciones son: ' % calificaciones
