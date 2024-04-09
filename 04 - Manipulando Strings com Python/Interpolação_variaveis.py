name = "Carlos"
age = 30
profile = "Analista de infraestrutura 1"
linguagem = "Java"

pessoa = {"name":"Carlos", "age": 30, "profile":"Analista de infraestrutura 1", "linguagem" : "Java" }

print("Old Style")
print()
print("Olá, me chamo %s. eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s!" % (name, age, profile, linguagem))
print()
print("Olá, me chamo {3}. eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}!".format(linguagem, profile, age, name))
print()
print("Olá, me chamo {name}. eu tenho {age} anos de idade, trabalho com {profile} e estou matriculado no curso de {linguagem}!".format(name=name,age=age, profile=profile,linguagem=linguagem ))
print()
print("Olá, me chamo {name}. eu tenho {age} anos de idade, trabalho com {profile} e estou matriculado no curso de {linguagem}!".format(**pessoa))
print()
print("modo utilizado atualmente")
print(f"Olá, me chamo {name}. eu tenho {age} anos de idade, trabalho com {profile} e estou matriculado no curso de {linguagem}!")
print()
PI=3.14159
print("Formatar String")
print("SEM FORMATAÇÃO")
print(PI)
print("FORMATADO")
#dessa forma não inseri nenhum número a esquerda
print(f"Valor de PI: {PI:.2f}")
#dessa forma não inseri a quantidade de espaço a esquerda nesse exemplo seria 10
print(f"Valor de PI: {PI:10.2f}")
