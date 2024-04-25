## Tuplas

Tuplas são estruturas de dados muito parecida com as listas, a principal diferença
é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através
da classe tuple, ou colocando valores separados por vírgula de parenteses.

#### Quando usar? 

Deve-se utilizar tuplas quando você quer uma garantia que o valor não seja alterado

### Acesso ao valores
A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices.
Contamos o índice de determinada sequência a partir do zero.

### Índices negativos
Sequências suportam indexação negativa. A contagem começa em -1.

### Tuplas aninhadas
Tuplas podem armazenar todos os tipos de objetos Python, portanto podemos ter tuplas que armazenam outras tuplas.
Com isso podemos criar estruturas bidimensionais(tabelas), e acessar informando os índices de linha e coluna.

### Fatiamento

Além de acessar elementos diretamente, podemos extrair um conjunto de valores sequência. Para isso basta passar o índice 
inicial e/ou final para acessar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

### Enumerate

Ás vezes é necessário saber qual o índice do objeto dentro do laço **for**. Para isso podemos usar a função **enumerate**.

### Metodos da classe list

* **.count()** - Contar a quantidade de ocorrências de um determinado elemento em uma lista.
* **.index()** - Mostra a posição do Index do elemento desejado
* **len()** - Retorna o número de elementos na lista
