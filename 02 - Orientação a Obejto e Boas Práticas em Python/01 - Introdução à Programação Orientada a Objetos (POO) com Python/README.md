# Programação orientada a objetos (POO)
Conhecer o paradigma de programação orientada a objetos.
### O que é POO?

#### Paradigmas de programação

Um paradigma de programação é um estilo e programação. Não é uma linguagem (Python, Java, C, etc), e sim a forma como você soluciona os problemas através do código.

#### Alguns paradigmas

- Imperativo ou procedural
- Funcional
- Orientado a eventos

## Programação orientada a objetos

O paradigma de programação orientada a objetos estrutura o código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais modular e extensível. Os dois conceitos chaves para aprender POO são: classes e objetos. 

## Classes e objetos

Aprender a utilizar classes e objetos com Python.

### Conceito de classes e objetos

Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente. Já os objetos podemos usá-los e eles possuem as características e comportamentos que foram definidos nas classes.


#### Classe

```
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")
```

#### Objeto
```
	cao_1 = Cachorro("chappie", "amarelo", False)
	cao_2 = Cachorro("Aladim", "branco e preto")

	cao_1.latir()

	print(cao_2.acordado)
	cao_2.dormir()
	print(cao_2.acordado)
```


## Construtores e destrutores
Entender o conceito de construtor e destrutor.
### Conhecendo os métodos __init__ e __del__

#### Método construtor

O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome __init__.

#### __init__

```
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
```

#### Método destrutor
O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários quanto em C++ porque o Pyton tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __del__.

#### __del__
```
class Cachorro:
    def __del__(self):
        print("Destruindo a instância")

c = Cachorro()
del c
```



