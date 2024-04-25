class Bicicleta():
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def buzina(self):
        print("PLIM PLIM ...")
    def parar(self):
        print("Parando bicicleta ...")
        print("bicicleta Parada!")
    def correr(self):
        print("Vrummmmmm ...")


    #def __str__(self):
    #    return f"Bicileta:\n Cor:{self.cor}\n Fabricante:{self.modelo}\n Ano:{self.ano}\n Valor:{self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {'\n '.join([f'{chave} = {valor}' for chave, valor 
                                                        in self.__dict__.items()])}"


b1 = Bicicleta("Amarela", "Caloi", 2024, 700, 5)



b1.buzina()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1)

b2 = Bicicleta("verde", "Monark", 2010, 400, 3)




