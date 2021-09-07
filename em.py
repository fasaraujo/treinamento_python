
# Copyright Francisco Arnaldo S. Araujo
# e-mail: netservicero@gmail.com
# technologist in electrical systems
# calcula vao regulador
# raiz(v1)^3+(v2)^2+(v3)^3.../v1+v2+v3)

import math

arnapegavao = 0
arnasomavao = 0
arnacubo = 0
arnasoma_cubo = 0
arna_again = 'S'

# funcao calcula componente horizontal do vento
#def vento(vao):
#    math.sqrt()

while arna_again == 'S':
    arnapegavao = float(input("informe o vão em metros..:"))
    arna_again = str(input("Continua [S/N]")).upper()
    arnasomavao += arnapegavao
    arnacubo += (arnapegavao **3)
    arnasoma_cubo += arnacubo
    arnacubo = 0
else:
    print("total do vao acumulado..: {}".format(arnasomavao))
    print("Vao regulador ..: {}".format(math.sqrt(arnasoma_cubo/arnasomavao)))



