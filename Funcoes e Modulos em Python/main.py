# Exercício 1: Arredondamento e Raiz Quadrada Módulo math
# Escreva um programa que solicite ao usuário um número decimal positivo. O programa deve calcular e
# exibir na tela:
# A raiz quadrada do número digitado;
# O valor arredondado para cima (utilizando a função adequada do módulo math );
# O valor arredondado para baixo (utilizando a função adequada do módulo math ).

# import math 

# def calcular_raiz_e_arredondar(numero):
#     raiz_quadrada = math.sqrt(numero)
#     arrendondar_cima = math.ceil(numero)
#     arrendondar_baixo = math.floor(numero)
#     return raiz_quadrada, arrendondar_cima, arrendondar_baixo

# numero = float(input("digite um número decimal positivo: "))
# if numero > 0:
#     raiz_quadrada, arredondar_cima, arredondar_baixo = calcular_raiz_e_arredondar(numero)

#     print(f"A raiz quadrada do número digitado é {raiz_quadrada:.2f}")
#     print(f"O valor arredondado para cima é {arredondar_cima}")
#     print(f"O valor arredondado para baixo é {arredondar_baixo}")
# else:
#     print("Erro: digite um número positivo.")



# Exercício 2: Calculadora de Área de Círculo Definição e Retorno
# Crie uma função chamada calcular_area_circulo(raio) que receba o raio de um círculo como
# parâmetro e retorne a área desse círculo.
# Dica: A fórmula da área é A = π × r
# 2
# . Utilize a constante math.pi .

# No fluxo principal do código, solicite o valor do raio ao usuário, chame a função criada e exiba o
# resultado final formatado com 2 casas decimais.

# import math

# def calcular_area_circulo(raio):
#     area = math.pi * raio**2
#     return area

# raio = float(input("Digite o valor do raio do círculo: "))
# area_circulo = calcular_area_circulo(raio)
# print(f"A área do círculo com raio {raio} é {area_circulo:.2f}")

# Exercício 3: Parâmetros e Condicionais (Maior de Três) Parâmetros & Estrutura de Decisão
# Escreva uma função chamada encontrar_maior(a, b, c) que receba três números inteiros como
# parâmetros e retorne qual deles é o maior valor.
# No código principal, peça 3 números ao usuário, execute a função criada e exiba na tela o valor
# retornado.

# def encontrar_maior(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# a = int(input("Digite o primeiro número inteiro: "))
# b = int(input("Digite o segundo número inteiro: ")) 
# c = int(input("Digite o terceiro número inteiro: "))

# maior_numero = encontrar_maior(a, b, c)
# print(f"O maior número entre {a}, {b} e {c} é: {maior_numero}")

# Exercício 4: Compreendendo Escopo de Variáveis Escopo Local vs Global
# Observe atentamente o código em Python abaixo e responda às questões sem executar o programa no
# computador:
# x = 10 # Variável 1
# def alterar_valor():
# x = 5 # Variável 2
# print(f"Valor dentro da função: {x}")
# alterar_valor()
# print(f"Valor fora da função: {x}")
# a) Qual será a saída exata impressa no console ao executar este código?
# RESPOSTA A:
# Valor dentro da função: 5
# Valor fora da função: 10

# b) Explique por que o valor de x fora da função não é alterado para 5, utilizando o conceito de Escopo
# de Variáveis (distinção entre escopo local e escopo global).
# RESPOSTA B:

# A variável global x = 10 foi declarada fora da função e pode ser acessada em diferentes partes do programa. 
# Já a variável x = 5, declarada dentro da função alterar_valor(), possui escopo local, ou seja, existe apenas
# dentro dessa função.
# Quando a função é executada, o Python utiliza o valor local 5 na impressão dentro da função. Ao terminar a 
# execução, a variável global continua com o valor original 10, pois ela não foi modificada.


# Exercício 5: Desafio Integrador (Cálculo de Hipotenusa) Organização & Módulos
# Crie um programa completo e bem estruturado (respeitando rigorosamente a ordem de: 1. Imports, 2.
# Funções e 3. Código Principal) para calcular a hipotenusa de um triângulo retângulo.
# Defina a função calcular_hipotenusa(cateto_a, cateto_b) que receba a medida dos catetos
# e retorne a hipotenusa calculada usando o Teorema de Pitágoras (h = √(a
# 2 + b
# 2
# )).

# No código principal, peça os valores dos catetos ao usuário, chame a função e imprima o resultado.

# import math


# def calcular_hipotenusa(cateto_a, cateto_b):
#     hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
#     return hipotenusa

# cateto_a = float(input("Digite o valor do cateto A: "))
# cateto_b = float(input("Digite o valor do cateto B: "))

# resultado = calcular_hipotenusa(cateto_a, cateto_b)
# print(f"a hipotenusa é {resultado:.2f}")
# print(f"o cateto A é {cateto_a:.2f} e o cateto B é {cateto_b:.2f}")