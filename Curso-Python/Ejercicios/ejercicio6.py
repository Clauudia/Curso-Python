#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

odioso = {numero : (bin(numero), hex(numero)) for numero in range(51) if bin(numero)[2:].count("1") & 1}
print odioso