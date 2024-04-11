Lista em Python podem armazenar de maneira sequencial qualquer tipo de objeto.
Podemos criar listas utilizando o construtor list, a função range ou colocando
valores separados por vírgula dentro de colchetes.
Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

### Listas aninhadas

Listas podem armazenar todos os tipos de Objetos Python, portanto podemos ter listas que armazenam outras listas.
Com isso podemos criar estruturas bidimensionais(tabelas), e acessar informando os índices de linha e coluna

### Fatiamento

Além de acessar elementos diretamente, podemos extrair um conjunto de valores sequência. Para isso basta passar o índice 
inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso

### Iterar Listas

A forma mais comum para percorer os dados de uma lista é utilizando o comando for

### Compreensão de listas

A compreensão de lista oferece uma sintaxe mais curta quanto você deseja: Criar uma nova lista
com base nos valores de uma lista existente(filho) ou gerar uma nova lista aplicando alguma modificação nos elementos de
uma lista existente.

### Metodos da classe list

* **.append()** - acrescentar novos valores a lista
* **.clear()** - limpar a lista
* **.copy()** - copiar uma lista igual porem com uma instacia diferente
* **.count()** - Contar a quantidade de ocorrências de um determinado elemento em uma lista.
* **.extend()** - juntar duas listas em uma só
* **.index()** - Mostra a posição do Index do elemento desejado
* **.pop()** - Retira o ultimo elemento da lista ou remove o elemento informado entre ().
* **.remove()** - Remove item da lista, porem exemplificamos com o nome do elemento.
* **.reverse()** - Colocar a lista ao contrario
* **.sort()** - Ordenar a lista alfabeticamente 
* **len()** - Retorna o número de elementos na lista
* **sorted()** - Cria uma nova lista ao realizar uma cópia da lista original e então ordena essa nova lista, sem afetar 
a lista original
