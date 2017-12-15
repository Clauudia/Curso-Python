#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

import re

ipv4 = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
correo = r"[a-zA-Z0-9] + (?:[\.\_-]?[a-zA-Z0-9]+)*@(?:[a-z]+\.)+[a-z]+"