class Cachorro():
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo Instância da classe.")
    def latir(self):
        print("Auauauau")

def criar_cachorro():
    c= Cachorro("Alfredo", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Meg", "Branco")

c.latir()

print("Olá Mundo")
del c
print("=====================================")
criar_cachorro()