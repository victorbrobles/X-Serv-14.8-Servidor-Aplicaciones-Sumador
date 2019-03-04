#!/usr/bin/python3

"""
webApp class
 Root for hierarchy of classes implementing web applications

 Copyright Jesus M. Gonzalez-Barahona and Gregorio Robles (2009-2015)
 jgb @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - February 2015
"""

from webapp import webApp

result = 0

class Calculadora(webApp):
	def parse(self, request):
		recurso = request.split()[1][1:]
		return recurso

	def process(self, parsedRequest):
		operador = parsedRequest[:parsedRequest.find("/")]
		num = parsedRequest[parsedRequest.find("/"):][1:]

		global result

		saved = result

		if operador == 'suma':
			signo = "+"
			result = int(saved) + int(num)
		elif operador == 'multi':
			signo = "*"
			result = int(saved) * int(num)
		elif operador == 'resta':
			signo = "-"
			result = int(saved) - int(num)
		elif operador == 'divis':
			signo = "/"
			result = int(saved) / int(num)
		else:
			return ("400 ERROR", "<html><body><h1>No existe la operacion " + str(operador) + "</h1></body></html>")

		return ("200 OK", "<html><body><h1>" + str(saved) + "  " + str(signo) + " " + str(num) + " = " + str(result) + "</h1></body></html>")

if __name__ == "__main__":
	testWebApp = Calculadora("localhost", 1238)


