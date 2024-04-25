class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {'\n '.join([f'{chave} = {valor}' for chave, valor
                                                         in self.__dict__.items()])}"
class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhão(Veiculo):

    def __init__(self, cor, placa, numero_rodas, carregado): #sobreescreve o construtor da classe pai
        super().__init__(cor, placa, numero_rodas) #Deixa claro que deseja utilizar o contrutor da classe pai
        self.carregado = carregado
    def esta_carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não,'} estou carregado")
    pass

moto = Motocicleta("Preta", "ABC-1234", 2)
moto.ligar_motor()

carro = Carro("Preta", "ABC-1234", 4)
carro.ligar_motor()

caminhao = Caminhão ("Roxo", "def-5678", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
