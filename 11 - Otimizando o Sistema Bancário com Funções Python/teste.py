# Função para adicionar um novo usuário ao dicionário de usuários
def adicionar_usuario(usuarios, nome, cpf, endereco):
    """
    Função para adicionar um novo usuário ao dicionário de usuários.

    Argumentos:
    usuarios: Dicionário de usuários.
    nome: Nome do usuário.
    cpf: CPF do usuário.
    endereco: Dicionário contendo o endereço do usuário.
    """
    usuarios[cpf] = {
        "Nome": nome,
        "CPF": cpf,
        "Endereço": endereco
    }

# Dicionário de usuários
usuarios = {}

# Função para criar um dicionário de endereço
def criar_endereco(logradouro, numero, bairro, cidade, estado):
    """
    Função para criar um dicionário de endereço.

    Argumentos:
    logradouro: Rua ou logradouro.
    numero: Número do endereço.
    bairro: Bairro.
    cidade: Cidade.
    estado: Estado (sigla).
    """
    endereco = {
        "Logradouro": logradouro,
        "Número": numero,
        "Bairro": bairro,
        "Cidade": cidade,
        "Estado": estado
    }
    return endereco

# Adicionar usuários
endereco1 = criar_endereco("Rua A", "123", "Bairro A", "Cidade A", "AA")
endereco2 = criar_endereco("Rua B", "456", "Bairro B", "Cidade B", "BB")

adicionar_usuario(usuarios, "Fulano", "111.222.333-44", endereco1)
adicionar_usuario(usuarios, "Ciclano", "222.333.444-55", endereco2)

# Exibir usuários
print("Usuários:")
for cpf, usuario in usuarios.items():
    print("\nCPF:", cpf)
    for chave, valor in usuario.items():
        if chave == "Endereço":
            print(chave + ":")
            for k, v in valor.items():
                print("  " + k + ":", v)
        else:
            print(chave + ":", valor)