'''
9. Crie um programa que faça a validação de json. O json
recebido pelo programa tem os seguintes dados, email e telefone:
{"email": "estevao@gmail.com", "celular": 61981751329}
Caso falte informação apresente erro. Caso venha campos
diferentes ou adicionais. Apresente erro.
'''
import json

def validar_json(dados):
    campos_necessarios = {"email", "celular"}
    try:
        dados_json = json.loads(dados)
    except json.JSONDecodeError:
        return "JSON inválido"

    campos_recebidos = set(dados_json.keys())
    if campos_recebidos == campos_necessarios:
        return "JSON válido"
    else:
        return "Erro: Campos faltando ou adicionais presentes"

dados = '{"email": "estevao@gmail.com", "celular": 61981751329}'
print(validar_json(dados))