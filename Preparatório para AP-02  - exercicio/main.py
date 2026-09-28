

# 1. Imports
import random


# 2. Definições de Funções
def gerar_nota_aleatoria():
    nota = random.randint(0,10)
    return nota
    
def verificar_situacao(nota):
    print(f"a nota foi {nota}")
    if nota >= 6:
        print("aluno aprovado")
    else:
        print("aluno reprovado")
# 3. Código Principal

nota = gerar_nota_aleatoria()

verificar_situacao(nota)