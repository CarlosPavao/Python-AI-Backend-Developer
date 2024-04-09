menu = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Qual valor deseja depositar: "))

        if deposito >= 0:
            saldo += float(deposito)
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("valor inválido, precisa ser maior que 0")

        print(saldo)


    elif opcao == "2":
        saque = float(input("Qual valor do seu saque:"))

        if saque <= saldo:
            if LIMITE_SAQUES > numero_saques:
                if saque <= limite:
                    saldo -= saque
                    numero_saques +=1
                    extrato += f"Saque: R$ {saque:.2f}\n"
                else:
                    print("O valor que deseja sacar é acima do limite, por favor selecione um valor mais baixo!")
            else:
                print("Limite de saques diários execido")
        else:
            print("Saldo insuficiente! ")
    elif opcao == "3":
        nome = "extrato"
        fim =""
        print(nome.center(50, "=").upper())
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(fim.center(50, "="))
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favot selecione novamente a operação desejada.")