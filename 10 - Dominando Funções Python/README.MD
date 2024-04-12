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

## Retornando Valores

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

## Argumentos nomeados

Funções também podem ser chamados usando argumentos nomeados da forma chave=valor

## Args e kwargs
Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos(*args e **kwargs), o método recebe
os valores como tupla e dicionário respectivamente


