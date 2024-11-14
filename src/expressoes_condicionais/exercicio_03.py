"""
3. Calculadora simples, Crie um programa que peça ao usuário
 dois números e uma operação (soma, subtração, multiplicação, divisão)
 e exiba o resultado.
"""

def calculadora(operador, numero_um, numero_dois):

    if operador == '+':
        return f'Resultado da soma: {numero_um + numero_dois}'
    
    elif  operador == '-':
        return f'Resultado da subtração: {numero_um - numero_dois}'
    
    elif  operador == '*':
        return f'Resultado da multiplicação: {numero_um * numero_dois}'
    
    elif  operador == '/':
        return f'Resultado da civisçao: {numero_um / numero_dois}'

print('O sistema irá solicitar uma operação matemática e dois números!')
print()

operador = str(input('Digite o operador: '))
numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite mais um número: '))

print(calculadora(operador, numero_um, numero_dois))

