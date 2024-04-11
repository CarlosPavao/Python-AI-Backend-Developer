#Filtro versão 1
numeros = [1, 30, 21, 2, 15, 20, 50, 151, 45]
pares = []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
print(pares)

#Filtro versão compreensão
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#Modificando Valores
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

print(quadrado)
#Modificando Valores versão compreensão
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)




