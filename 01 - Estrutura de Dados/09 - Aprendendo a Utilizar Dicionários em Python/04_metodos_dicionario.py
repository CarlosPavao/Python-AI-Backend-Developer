contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1111-2222"},
    "carlos@gmail.com": {"nome": "Carlos", "telefone": "2222-2222"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "carol@gmail.com": {"nome": "Carol", "telefone": "1111-5555"},
}
contatos2 = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1111-2222"},
    "carlos@gmail.com": {"nome": "Carlos", "telefone": "2222-2222"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "carol@gmail.com": {"nome": "Carol", "telefone": "1111-5555"},
}

print(" {}.clear ".center(20, "#"))
print(contatos2)
contatos2.clear()
print("Impressão contatos2: ", contatos2)

print(" {}.copy ".center(20, "#"))
print("Impressão contatos2: ", contatos2)
contatos2 = contatos.copy()
print(contatos2)

print(" {}.fromkeys ".center(20, "#"))
result = contatos.fromkeys(["cidade", "estado"])
print(result)
contatos.fromkeys(["cidade", "estado"], "vazio")
print(contatos)

print(" {}.get ".center(20, "#"))
#Quando a chave não existe retornar erro: KeyError
#contatos["chave"]

resultado = contatos.get("nome") #retorna None quando não econtra por padrão
print("Retorno padrão:", resultado)
resultado = contatos.get("nome", {}) #alterando a forma que vai retornar quando não encontrar
print("Retorno alterado:", resultado)
resultado = contatos.get("carlos@gmail.com")
print(resultado)

print(" {}.items ".center(20, "#"))

print(contatos.items())

print(" {}.keys ".center(20, "#"))
resultado = contatos.keys()
print(resultado)

print(" {}.pop ".center(20, "#"))
resultado = contatos.pop("guilherme@gmail.com")#Quando existe a chave ele retorna o valor que será removido
print(resultado)
resultado = contatos.pop("guilherme@gmail.com", "Valor não encontrado") #Quando a chave não existe irá retornar o valor que for definido após a virgula
print(resultado)

print(" {}.popitem ".center(20, "#"))
print(contatos)
contatos.popitem()
print(contatos)

print(" {}.setdefault ".center(20, "#"))
contatos.setdefault("nome", "Giovanna")
print(contatos)
contatos.setdefault("idade", 28)
print(contatos)

print(" {}.update ".center(20, "#"))
contatos.update({"giovanna@gmail.com": {"nome": "Gio"}})
print(contatos)
contatos.update({"maria@gmail.com": {"nome": "Gio", "telefone": "96855-8431"}})
print(contatos)

print(" {}.values ".center(20, "#"))
resultado = contatos.values()
print(resultado)

print(" {}.in ".center(20, "#"))
resultado = "guilherme@gmail.com" in contatos
print(resultado)
resultado = "carlos@gmail.com" in contatos
print(resultado)
resultado = "giovanna@gmail.com" in contatos
print(resultado)
resultado = "idade" in contatos["giovanna@gmail.com"]
print(resultado)
resultado = "telefone" in contatos["carlos@gmail.com"]
print(resultado)

print(" {}.del ".center(20, "#"))
del contatos["carlos@gmail.com"]["telefone"]
print(contatos)
del contatos["maria@gmail.com"]
print(contatos)
