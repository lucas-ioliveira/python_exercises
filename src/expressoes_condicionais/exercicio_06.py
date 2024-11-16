"""
6. Escreva um verificador de validade de senha. O programa deve
 receber uma senha e verificar se ela atende aos seguintes critérios:
 Pelo menos uma letra maiúscula
 Pelo menos uma letra minúscula
 Pelo menos um número
Pelo menos um símbolo especial
"""

def validar_senha(senha):
    if len(senha) < 8:
        return "Senha inválida: deve ter no mínimo 8 caracteres."
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False
    simbolos_especiais = "!@#$%^&*(),.?\":{}|<>"
    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_numero = True
        elif char in simbolos_especiais:
            tem_simbolo = True
    
    if not tem_maiuscula:
        return "Senha inválida: deve conter pelo menos uma letra maiúscula."
    if not tem_minuscula:
        return "Senha inválida: deve conter pelo menos uma letra minúscula."
    if not tem_numero:
        return "Senha inválida: deve conter pelo menos um número."
    if not tem_simbolo:
        return "Senha inválida: deve conter pelo menos um símbolo especial."
    
    return "Senha válida"

senha = input("Digite uma senha: ")
print(validar_senha(senha))