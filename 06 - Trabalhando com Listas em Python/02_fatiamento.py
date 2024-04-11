#FATIAMENTO funciona na estrutura inicio:meio:fim
lista = ["P", "Y", "T", "H", "O", "N"]

# Mostrar os elementos a partir do segundo que no caso seria o "T"
print("2:", lista[2:])
#Mostra somente os dois primeiros
print(":2", lista[:2])
#Mostra do primeiro elemento até o 3 nesse exemplo seria 'Y' 'T'
print("1:3", lista[1:3])
# Mostra os elementos pulando 0 é o inicio - 3 é até onde ele pode ir
# 2 é de quantos em quantos ele vai andar
print("1:3", lista[0:3:2])
print("::", lista[::])
# Mostrar os elementos de tras para frente
print("::-1", lista[::-1])



