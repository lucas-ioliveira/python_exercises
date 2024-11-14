"""
4. Escreva um programa que calcule o Índice de Massa Corporal
 (IMC) e classifique o usuário como abaixo do peso, peso normal,
 sobrepeso ou obeso.
"""

def calculo_imc(peso, altura):
    resultado = peso / (altura ** 2)

    if resultado < 18.5:
        return f'O resultado do calculo é: {resultado:.2f}, você está abaixo do peso'
    
    elif resultado < 24.9:
        return f'O resultado do calculo é: {resultado:.2f}, você está com o peso normal'
    
    elif resultado < 29.9:
        return f'O resultado do calculo é: {resultado:.2f}, você está com sobrepeso'
    
    elif resultado < 34.9:
        return f'O resultado do calculo é: {resultado:.2f}, você está com obsidade grau 1'
    
    elif resultado < 39.9:
        return f'O resultado do calculo é: {resultado:.2f}, você está com obsidade grau 2'
    
    elif resultado >= 40 :
        return f'O resultado do calculo é: {resultado:.2f}, você está com obsidade grau 3'

peso = float(input('Digite o seu peso (KG): '))
altura = float(input('Digite a sua altura (M): '))

print(calculo_imc(peso, altura))