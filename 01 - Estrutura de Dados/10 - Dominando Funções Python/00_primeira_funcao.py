def exibir_mensagem():
    print("Olá Mundo!")

#Obrigatório passar o argumento para execução da função
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

#Declarando o valor não se torna obrigatorio para execução da função
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Carlos")
exibir_mensagem_3()
exibir_mensagem_3(nome="Carlos")