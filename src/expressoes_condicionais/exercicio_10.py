'''
10. Faça um validador de CPF.
'''

def validador_cpf(cpf: str) -> str:
    if isinstance(cpf, str):
        if '.' in cpf or '-' in cpf:
            cpf_recebido = cpf.replace('.', '').replace('-', '').strip()
        else:
            cpf_recebido = cpf
        
        if len(cpf_recebido) < 11:
            return 'O cpf recebido é inválido.'
        
        if not cpf_recebido.isdigit():
            return f'O cpf: {cpf_recebido} recebido é inválido.'
    
        return f'O cpf: {cpf_recebido} é válido.'
    return f'O cpf: {cpf} recebido é inválido.'

print(validador_cpf(int('15870072743')))