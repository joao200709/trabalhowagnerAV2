# Questão 4 - Verificador de Números Pares e Ímpares
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.

numero = int(input("Digite um número: "))

def parOuImpar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
print(parOuImpar(numero))