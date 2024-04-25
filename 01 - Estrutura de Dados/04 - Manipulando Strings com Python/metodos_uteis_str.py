curso = "pYthon"

#tudo Maiusculo
print(curso.upper())

#tudo Minusculo
print(curso.lower())

#Primeira letra Maiuscula
print(curso.title())

print()

curso = "   Python  "
#Remove espaços em branco
print(curso.strip())

#Remove espaços em branco da direita
print(curso.lstrip())

#Remove espaços em branco da esquerda
print(curso.rstrip())

print()

curso = "Python"

#Centraliza a Strinf e insere o caracter que deseja matendo o numero de caracter informado nesse exemplo seria 10
print(curso.center(10, "#"))

#Junção na string anda item por item e coloca o caracter que foi informado
print(".".join(curso))

