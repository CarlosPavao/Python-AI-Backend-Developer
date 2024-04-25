from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "LG"
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "Samsung"

controle = ControleTV()

controle.ligar()
controle.desligar()
print(controle.marca)
controle2 = ControleArCondicionado()

controle2.ligar()
controle2.desligar()
print(controle2.marca)
