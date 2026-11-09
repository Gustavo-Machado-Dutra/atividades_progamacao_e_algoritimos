# frutas = []
# frutas.append("maça")
# frutas.append("pera")
# frutas.append("uva")
# frutas.append("abacaxi")
# print(frutas)

pares = []
numero = 0

for i in range(11):
    numero = i
    if numero % 2 == 0:
        pares.append(numero)
        print(pares)
    else:
        print(f'impar {i}')