'''
8. Jogo de Pedra-Papel-Tesoura: Crie um jogo para jogar contra o
computador de Pedra-Papel-Tesoura usando instruções condicionais e
loops. Permita que o usuário escolha sua jogada e determine o
vencedor com base na lógica do jogo. Implemente um sistema de
pontuação para acompanhar as vitórias e derrotas de cada jogador.
'''
import random

partidas_jogadas = 0
derrotas = 0
empates = 0
vitorias = 0

while True:
    print('-- Jogo pedra papel tesoura --')
    print()
    
    menu = '''
    [1] - Iniciar
    [2] - ver pontuação
    [3] - encerar
    '''
    print(menu)
    opcao_escolhida_menu = input('Escolha uma das opções: ')
    print()
    
    opcoes_de_jogo = ['Pedra', 'Papel', 'Tesoura']
    
    if int(opcao_escolhida_menu) == 3:
        print('-- Jogo encerrado --')
        break
    
    elif int(opcao_escolhida_menu) == 2:
        print('-- Pontuação --')
        print(f'Total de partidas jogadas: {partidas_jogadas}')
        print(f'Total de vitórias: {vitorias}')
        print(f'Total de derrotas: {derrotas}')
        print(f'Total de empates: {empates}')
        continue

    elif int(opcao_escolhida_menu) == 1:
        partidas_jogadas += 1
        print('Escolha uma das opções')
        print()
        print(opcoes_de_jogo)
        computador = random.choice(opcoes_de_jogo)
        opcao_escolhida_jogador = input('Digite aqui: ')
        if opcao_escolhida_jogador.title() == computador:
            empates += 1
            print("Empate!")
            print(f'Jogador escolheu: {opcao_escolhida_jogador}.')
            print(f'Computador escolheu: {computador}.')
            print()
            continue
        
        elif opcao_escolhida_jogador.title() == 'Pedra' and computador == 'Tesoura' or opcao_escolhida_jogador.title() == 'Papel' and computador == 'Pedra':
            vitorias += 1
            print('Jogador ganhou!')
            print(f'Jogador escolheu: {opcao_escolhida_jogador}.')
            print(f'Computador escolheu: {computador}.')
            print()
            continue

        else:
            derrotas += 1
            print('Computador ganhou!')
            print(f'Jogador escolheu: {opcao_escolhida_jogador}.')
            print(f'Computador escolheu: {computador}.')
            print()
            continue
        
    else:
        print('Opção inválida!')
        continue

