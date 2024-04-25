## Conjuntos

um set é um coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar
itens duplicados de um iterável.

### Acessando Dados 
Conjuto em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário converter o
conjunto para lista.

### Iterar 

A forma mais comum para percorrer os dados de conjunto é ultilizando o comando for

### Enumerate

Ás vezes é necessário saber qual o índice do objeto dentro do laço **for**. Para isso podemos usar a função **enumerate**.

### Metodos da classe SET

* **{}.union** - fazer a união de dois SET
* **{}.intersection** - Aparecer somente os valores iguais dos dois sets
* **{}.difference** - Retirar os numeros diferente entre os dois conjuntos
* **{}.symmetric_difference** - Pegar todos os elementos que não está na intersecção
* **{}.issubset()** - Retorna True se todos os itens do conjunto especificado existirem no conjunto original, caso 
contrário, retorna False.
* **{}.issuperset()** - Retorna True se todos os itens do conjunto especificado existirem no conjunto original, caso 
contrário, retorna False.
* **{}.isdisjoint()** - Retorna True se os conjuntos não tiverem nenhum elemento em comum
* **{}.add()** - Verificar se tem o valor determinado e em caso negativo acrescenta aquele valor ao conjunto se já 
possuir ele ignora
* **{}.pop()** - Retira o primeiro elemento da lista ou remove o elemento informado entre ().
* **{}.remove()** - Remove item da lista que informamos quando chamamos o metodo, porem se não existir o metodo ele 
retorna erro
* **{}.discard()** - Descartar um número do conjunto se falar um valor que não existe não retorna nenhum erro apenas é 
ignorado
* **{}.len()** - Descobrir o tamanho do conjunto
* **in** - verificar se determinado número está no conjunto retorna true se existir e caso contrario false