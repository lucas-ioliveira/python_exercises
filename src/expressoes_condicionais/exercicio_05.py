"""
5. Crie um programa que verifique se um número inserido pelo
 usuário é primo ou não.
"""

def verificar_numero_primo(numero):
    if numero < 2:
        return f'O número {numero} não é primo.'
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return f'O número {numero} não é primo.'
    
    return f'O número {numero} é primo.'

numero = int(input('Digite um número: '))
print(verificar_numero_primo(numero))
