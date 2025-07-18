'''
7. Jogo de Adivinhação: Escreva um programa que gere um
número aleatório entre 1 e 100 e desafie o usuário a adivinhá-lo. O
programa deve fornecer dicas ao usuário, informando se o seu palpite
está acima, abaixo ou igual ao número secreto. O jogo termina quando
o usuário acerta o número ou atinge um limite máximo de tentativas.
'''
from random import randint

numero_secreto: int = randint(1, 100)
tentativas: int = 0

while tentativas < 10:
    numero_do_usuario = int(input('Adivinhe o número secreto entre 1 e 100: '))
    tentativas += 1

    if numero_do_usuario == numero_secreto:
        print(f'Parabéns, você acertou o número secreto: {numero_secreto} em {tentativas} tentativas.')
        break
    
    elif numero_do_usuario > numero_secreto:
        print(f'O número secreto é menor, você já realizou {tentativas} tentativas.')
    
    elif numero_do_usuario < numero_secreto:
        print(f'O número secreto é maior, você já realizou {tentativas} tentativas..')
    
print('Acabou as suas tentativas.')