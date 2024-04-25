import textwrap

def menu():
    menu = """

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tListar Usúarios
    [0]\tSair

    => """
    return input(textwrap.dedent(menu))

def sacar(*, saldo, valor_saque, extrato, limite, quantidade_de_saques, limite_saques):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saque = quantidade_de_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saque:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        quantidade_de_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato
def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(50, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("".center(50, "="))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += float(deposito)
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print("\n==== Deposito realizado com sucesso! ====")
    else:
        print("valor inválido, precisa ser maior que 0")
    return saldo, extrato

def add_user(usuarios, nome, cpf, data_nascimento, endereco):
    usuarios[cpf] = {
        "Nome": nome,
        "CPF": cpf,
        "Data": data_nascimento,
        "Endereço": endereco
    }
def new_user(usuarios):
    cpf_sem_verificacao = input("Informe seu CPF")
    cpf = cpf_sem_verificacao.replace(".", "").replace("-", "")
    usuario = filter_user(cpf, usuarios)

    if usuario:
        print("Usuário já existente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    rua = input("Informe o logradouro: ")
    numero_casa = input("Informe o número da casa: ")
    bairro = input("Informe o Bairro: ")
    cidade = input("Informe o cidade: ")
    estado = input("Informe a sigla do estado: ")

    enderecos = new_adrees(rua, numero_casa, bairro, cidade, estado)
    add_user(usuarios, nome, cpf, data_nascimento, enderecos)

    print("=== Usuário criado com sucesso! ===")

    return usuarios

def filter_user(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios.values() if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

    name = input("Qual o seu nome: ")
    data_nasc = input("Data de Nascimento: ")

    user = {
        "CPF": {"nome": "name", "nascimento": "data_nasc"},
    }

    print("Usuario criado")

def new_adrees(logradouro, numero, bairro, cidade, estado):
    adress = {
        "Logradouro": logradouro,
        "Número": numero,
        "Bairro": bairro,
        "Cidade": cidade,
        "Estado": estado
    }
    return adress

def imprimir_user(usuarios):
    print("Usuários cadastrados:")
    for cpf, usuario in usuarios.items():

        for chave, valor in usuario.items():
            if chave == "Endereço":
                print(chave + ":")
                for k, v in valor.items():
                    print("  " + k + ":", v)
            else:
                print(chave + ":", valor)


def new_account(agencia, numero_conta, usuarios):
    cpf_sem_verificacao = input("Qual CPF deseja criar a conta? ")
    cpf = cpf_sem_verificacao.replace(".", "").replace("-","")
    usuario = filter_user(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


    print("Usuário Não encontrado com cpf informado, por favor criar primeiro o usuario!")

def listar_contas(contas):
    for conta in contas:
        nome_titular = conta['usuario']['Nome']  # Acessando apenas o nome do titular da conta
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{nome_titular}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = {}
    contas = []
    while True:

        opcao = menu()

        if opcao == "1":
            deposito = float(input("Qual valor deseja depositar: "))
            saldo, extrato = depositar(saldo, deposito, extrato)





        elif opcao == "2":
            valor_saque = float(input("Qual valor do seu saque:"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                limite=limite,
                quantidade_de_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )


        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = new_account(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao =="5":
            listar_contas(contas)
        elif opcao =="6":
            usuarios = new_user(usuarios)
        elif opcao == "7":
            imprimir_user(usuarios)
        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favot selecione novamente a operação desejada.")

main()