saldo = 100
saque = float(input("\nDigite o valor do saque:\n "))
cheque_especial = 1000.0
tipo_conta = str(input("Conta normal? \n[1] - SIM \n[2] - NÃO \n"))
conta_Universitaria = False
conta_normal = False

if tipo_conta == "1":
  conta_normal = True
else:
  conta_Universitaria = True

if conta_normal:
  if saldo >= saque:
    print("Saque realizado com sucesso!")
  elif saque <= (saldo + cheque_especial):
    print("Saldo insuficiente!")
elif conta_Universitaria:
  if saldo >= saque:
    print("Saque realizado com sucesso!")
  else:
    print("Saque não realizado!")
