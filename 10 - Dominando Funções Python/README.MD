## Funções

Função é um bloco de código identificado por um nome e pode receber uma lista de parâmentros, esses parâmetros podem ou
não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar 
baseado em funções, é o mesmo qe dizer que estamos programando de maneira estruturada

Em python quando passo uma variavel desse forma:
```
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")
```
Para chamar a mesma é necessario informar uma variavel nome, podem podemos declarar da seguinte forma:

```
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")
```

Dessa forma se torna opcional no momento que chamar a função declarar uma variavel. No caso de ser não informar uma 
variável ela irá assumir o nome que está declarado quando foi criado a função

### Retornando Valores

Para retornar um valor, utilizamos a palavra reservada return.
Toda função Python retorna None por padrão. Diferente de outras linguagens de programação, em Python uma função pode
retornar mais de um valor.

#### Retornando um único Valor
```
def calcular_total(numeros):
    return sum(numeros)   
```
#### Retornando mais de 1 valor
```
def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor
```
O retorno nesse cenário é em forma de tupla.

### Argumentos nomeados

Funções também podem ser chamados usando argumentos nomeados da forma chave=valor

### Args e kwargs
Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos(*args e **kwargs), o método recebe
os valores como tupla e dicionário respectivamente

### Parâmetros especiais
Por padrão, argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome. Para
uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passado, assim um
desenvolvedor preocsa apenas olhar para a definição da função para determinar se os itens são passados **por posição, 
por posição e nome, ou por nome.**

#### Parametro por posição
````
criar_carro("Palio", 1999, "ABC-1234")
````
Não é necessário declarar nada somente colocar na ordem que a função foi criafa

#### Parametro nomiado
````angular2html
(marca="Fiat", motor="1.0", combustivel="Gasolina")
````
Necessário passar chave=valor

### Objetos de primeira classe

Em Python tudo é objeto, dessa forma **funções também são objetos** o que as tornam objetos de primeira classe. Com isso
podemos **atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estruturas de 
dados**(listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função(closures).

### Escopo local e escopo global

Python trabalha com escopo local e global, dentro do bloco função o escopo é local. Portanto, alterações ali feitas em 
objetos imutáveis serão perdidas quanto o método terminar de ser executado. Para usar objetos globais utilizamos a 
palavra-chave **global**, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
Essa **NÃO é uma boa prática e deve ser evitada**