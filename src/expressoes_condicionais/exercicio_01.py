"""
1. Crie um programa que classifique uma pessoa como criança (0
12 anos), adolescente (13-19 anos), adulto (20-64 anos) ou idoso (65
 anos ou mais) com base na idade inserida.
"""

def classificar_idade(age:int):

    if age < 0:
        return 'Idade invalida'

    elif age <= 12:
        return 'Com base na idade fornecida, sua classificação é: Criança'

    elif age >= 13 and age < 19:
        return 'Com base na idade fornecida, sua classificação é: Adolecente'

    elif age >= 20 and age < 64:
        return 'Com base na idade fornecida, sua classificação é: Adulto'

    else:
        return 'Com base na idade fornecida, sua classificação é: Idoso.'

age = int(input("Digite a sua idade: "))
print(classificar_idade(age))