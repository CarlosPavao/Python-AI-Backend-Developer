class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return Pessoa(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa("Carlos", 31)
print(p.nome, p.idade)
p2= Pessoa.criar_de_data_nascimento(1993,10,15, "Carlos Pavão")

print(p2.e_maior_idade(p2.idade))