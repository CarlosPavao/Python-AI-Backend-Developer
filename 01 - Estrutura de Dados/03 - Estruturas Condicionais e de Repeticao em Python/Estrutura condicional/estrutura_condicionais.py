print(
    "A estrutura condicional é uma estrutura de controle que permite que um programa execute diferentes blocos de código quando determinadas condições são atendidas."
)

saldo = 2000.0
saque = float(input("\nDigite o valor do saque: "))

print("\nestrutura if")
if saldo >= saque:
  print("Saque realizado com sucesso!")

if saldo < saque:
  print("Saldo insuficiente!")

print("\nestrutura if/else")

if saldo >= saque:
  print("Saque realizado com sucesso!")
else:
  print("Saldo insuficiente!")

print("\nestrutura if/elif/else")

opcao = int(input("\nInforme uma opção: \n[1] - Saque \n[2] - Extrato \n"))

if opcao == 1:
  valor = float(input("Informe a quantia do sa que: "))
elif opcao == 2:
  print("Exibindo o extrato ...")
else:
  sys.exit("Opção inválida!")

print("\nIf aninhado")

