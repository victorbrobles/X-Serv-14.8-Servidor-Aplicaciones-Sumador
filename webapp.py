#!/usr/bin/python3

"""
webApp class
 Root for hierarchy of classes implementing web applications

 Copyright Jesus M. Gonzalez-Barahona and Gregorio Robles (2009-2015)
 jgb @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - February 2015
"""

import socket

class webApp():
   

    def parse(self, request):
        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body></body></html>")

    def __init__(self, hostname, port):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        mySocket.listen(5)

        result = 0

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            request = str(recvSocket.recv(2048))
            print(request)
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print('Answering back...')
            recvSocket.send(b"HTTP/1.1 " + bytes(returnCode, "utf-8") + b" \r\n\r\n"
                            + bytes(htmlAnswer, "utf-8") + b"\r\n")
            recvSocket.close()











