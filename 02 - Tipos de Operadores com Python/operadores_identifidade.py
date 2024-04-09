print("operadores para comparar se os objetos testados usam a mesma região de memoria")

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print("curso is nome_curso = ", curso is nome_curso)

print("curso is not nome_curso = ", curso is not nome_curso)

print("saldo is limite= ", saldo is limite)

saldo = 500
saldo +=300
print(saldo)
