contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1111-2222"},
    "carlos@gmail.com": {"nome": "Carlos", "telefone": "2222-2222"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "carol@gmail.com": {"nome": "Carol", "telefone": "1111-5555"},
}

#Acessando os dados
telefone = contatos["giovanna@gmail.com"]["telefone"]
print(telefone)

dados = contatos["carlos@gmail.com"]
print(dados)