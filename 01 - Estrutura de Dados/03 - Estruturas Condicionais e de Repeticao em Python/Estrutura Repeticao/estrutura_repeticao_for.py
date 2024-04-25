print(
    "São Estruturas utilizadas para repetir um trecho do código um determinado número de vezes. o Número pode ser conhecido previamente ou determinado através de uma expressão lógica."
)

texto = input("Informe um texto: \n")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end = "")

print()


print("Exemplo utilizando a função built-in range\n")
#primeiro número representa de onde vai iniciar a conta, nesse exemplo seria o 1
print(list(range(4)))

#segundo número representa até onde vai a conta, nesse exemplo seria o 24
for numero in range(1, 25):
  print(numero, end = " ")


print()
#terceiro número representa de quanto em quanto vai a conta, nesse exemplo seria de 5 em 5
for numero in range(0, 51, 5):
  print(numero, end = " ")

#somente um unico número é obragatorio, os demais são opcionais