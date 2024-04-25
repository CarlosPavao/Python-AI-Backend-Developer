import re


def validate_numero_telefone(phone_number):
    # Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    telefone_valido = r'\(\d{2}\) 9\d{4}-\d{4}'

    # Use re.fullmatch() para verificar se o número de telefone corresponde ao padrão definido:
    if re.fullmatch(telefone_valido, phone_number):
        # Se corresponder, retorne que o número de telefone é válido:
        return "Número de telefone válido."
    else:
        # Caso contrário, retorne que o número de telefone é inválido:
        return "Número de telefone inválido."


# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()

# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)
