
# Francisco calcula vao regulador
# Raiz((v1)^3+(v2)^3+(v3)^3..../v1+v2+v3....)

import math

arnapegacota = 0
arnasoma = 0
arnacubo = 0
arnaconta_cubo = 0
arnacontinua = "S"

while arnacontinua == "S":
    arnapegacota = float(input("Entre com o vao em [metros] entre postes..: "))
    arnacontinua = str(input("Proximo vao [S/N]")).upper()
    arnasoma += arnapegacota

    arnacubo = arnacubo + (arnapegacota ** 3)
    arnaconta_cubo += arnacubo
    arnacubo = 0
else:
     print("Vao acumulado em metros..: {}".format(arnasoma))
     print("Vao Regulador.: {}".format(math.sqrt(arnaconta_cubo/arnasoma)))

# Entra com parametros gerais

# Velocidade do vento (m/s)
# Diametro do cabo (mm)
# Peso do cabo (kg/km)
# Flecha (%)
# Resultado = tracao [kfg]

arnavento = 0
arnadimfo = 0
arnapesofo = 0
arnaflecha = 0

#arnavento = float(input("Entre com velocidade do vento [m/s] ..:"))
#arnadimfo = float(input("Entre com diametro do cabo [mm] ..:"))
#arnapesofo = float(input("Entre com peso do cabo [kg/km] ..:"))
arnaflecha = float(input("Entre com a flecha [%]..:"))

print("flecha %..: {}".format(arnaflecha/100))



#for mostra in range(1,5):
#    print(mostra)
#print("fim")

#familia = ["Matheus", "Ryan", "Renan"]

#for membros in familia:
#    print(membros)
#print("fim")