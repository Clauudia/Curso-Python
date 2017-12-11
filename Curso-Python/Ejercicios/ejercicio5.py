#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import re

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION
c = ","
res =c.join(map((lambda lista: lista.upper()), (filter((lambda x: 'i' in x), ((lambda w,x,y,z: w + x + y + z) (sistemas, op_interna, incidentes, auditorias))))))
print res