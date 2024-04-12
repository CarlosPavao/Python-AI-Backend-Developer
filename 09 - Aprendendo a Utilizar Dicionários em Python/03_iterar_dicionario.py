contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1111-2222"},
    "carlos@gmail.com": {"nome": "Carlos", "telefone": "2222-2222"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "carol@gmail.com": {"nome": "Carol", "telefone": "1111-5555"},
}

for chave in contatos:
    print(chave, contatos[chave])
print("===================================")
for chave, valor in contatos.items():
    print(chave, valor)