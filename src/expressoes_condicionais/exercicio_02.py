"""
2. Escreva um programa que verifique se um número inserido pelo
 usuário é par ou ímpar.
"""

def par_ou_impar(numero):

    if numero % 2 == 0:
        return f'Você digitou o número: {numero} e ele é par'
    else:
        return f'Você digitou o número: {numero} e ele é impar'

numero = int(input("Digite um número: "))
print(par_ou_impar(numero))