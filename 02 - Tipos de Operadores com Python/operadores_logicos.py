saldo = 1000
saque = 200
limite = 150
conta_especial = True

print("Saldo é maior ou igual ao saque: ", saldo>=saque)

print("Saldo é menor ou igual ao saque: ", saldo<=saque)

print("operador and")
print("Saldo é maior ou igual ao saque e saque menor que limite: ", saldo>=saque and saque<=limite)

print("operador or")
print("Saldo é maior ou igual ao saque ou saque menor que limite: ", saldo>=saque or saque<=limite)

print("Operador de negação")
contatos_emergencia=[]
print("not 1000>1500 - ", not 1000>1500)

print("not contatos_emergencia - ", not contatos_emergencia)

print("not 'saque 1500' - ", not "saque 1500" )

print("not "" - ", not "" )


print("Priorização das operações utilizando Parênteses ")

print("Saldo é maior ou igual ao saque e saque menor ou igual ao limite ou é conta especial e saldo é maior ou igual ao saque: ")

exp = saldo>=saque and saque<=limite or conta_especial and saldo >= saque
print("saldo>=saque and saque<=limite or conta_especial and saldo >= saque = ", exp)

exp2 = (saldo>=saque and saque<=limite) or (conta_especial and saldo >= saque)
print("(saldo>=saque and saque<=limite) or (conta_especial and saldo >= saque) = ", exp2)
