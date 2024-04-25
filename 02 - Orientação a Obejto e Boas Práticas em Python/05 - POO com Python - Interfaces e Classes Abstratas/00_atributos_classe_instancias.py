class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valor(*objs):
    for obj in objs:
        print(obj)

estudante = Estudante("Guilherme", 1)
estudante2 = Estudante("Maria", 2)


mostrar_valor(estudante, estudante2)


Estudante.escola = "PYTHON"
estudante.matricula = 3
mostrar_valor(estudante, estudante2)