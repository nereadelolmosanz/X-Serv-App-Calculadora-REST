#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Nerea Del Olmo Sanz - GITT
Ejercicio 9.5
Calculadora simple, versión REST
Operaciones aritméticas básicas: suma, resta, multiplicación y división.
Herencia de clase webbApp
"""

import webapp


class calculatorApp (webapp.webApp):

    def parse(self, request):
        verb = request.split()[0]

        #Si es una división, x/y:
        if verb == "GET" and len(request.split("/")[1].split())==1:
            resource = request.split("/")[1].split()[0]
            resource += ("/")
            resource += request.split("/")[2]
            resource = resource.split()[0]
        #Para el resto de operaciones:    - si es PUT, da igual su valor
        else:
            resource = request.split("/")[1].split()[0]

        body = request.split()[-1]
        return (verb, resource, body)

    def process(self, parsedRequest):
        (verb, resource, body) = parsedRequest
        if verb == "GET":
            try:
                if (self.operation != resource):
                    httpCode = "400 BAD REQUEST"
                    htmlAnswer = ("GET operation is different to PUT operation\n")
                else:
                    try:
                        if (len(resource.split('+')) == 2):
                            result = (float(resource.split("+")[0]) +
                                      float(resource.split("+")[1]))
                            httpCode = "200 OK"
                            htmlAnswer = ("Your operation is:\n" + str(resource)
                                          + "=" + str(result))
                        elif (len(resource.split('-')) == 2):
                            result = (float(resource.split("-")[0]) -
                                      float(resource.split("-")[1]))
                            httpCode = "200 OK"
                            htmlAnswer = ("Your operation is:\n" + str(resource)
                                          + "=" + str(result))
                        elif (len(resource.split('*')) == 2):
                            result = (float(resource.split("*")[0]) *
                                      float(resource.split("*")[1]))
                            httpCode = "200 OK"
                            htmlAnswer = ("Your operation is:\n" + str(resource)
                                          + "=" + str(result))
                        elif (len(resource.split('/')) == 2):
                            result = (float(resource.split("/")[0]) /
                                      float(resource.split("/")[1]))
                            httpCode = "200 OK"
                            htmlAnswer = ("Your operation is:\n" + str(resource)
                                          + "=" + str(result))
                        else:
                            httpCode = "400 BAD REQUEST"
                            htmlAnswer = "Operation not available. "
                            htmlAnswer += "Use num1+num2, "
                            htmlAnswer += "Use num1-num2, "
                            htmlAnswer += "Use num1*num2, "
                            htmlAnswer += "Use num1/num2, "

                    except ValueError:
                        httpCode = "400 BAD REQUEST"
                        htmlAnswer = "Only float type available."
                    except AttributeError:
                        httpCode = "400 BAD REQUEST"
                        htmlAnswer = "No previous data"
            except AttributeError:
                self.operation = ""
                httpCode = "400 BAD REQUEST"
                htmlAnswer = "<h1>Use PUT first.</h1>"

        elif verb == "PUT":
            self.operation = body
            httpCode = "200 OK"
            htmlAnswer = "Operation recieved:\n" + str(self.operation)
        else:
            httpCode = "400 BAD REQUEST"
            htmlAnswer = "Invalid operation. Use PUT or GET."
        return (httpCode, htmlAnswer)

if __name__ == "__main__":
    testwebApp = calculatorApp("localhost", 1234)
