#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

odioso = {numero : tuple(bin(numero), hex(numero)) for numero in str(bin(numero in range(51))).count("1")%2 == 1}
