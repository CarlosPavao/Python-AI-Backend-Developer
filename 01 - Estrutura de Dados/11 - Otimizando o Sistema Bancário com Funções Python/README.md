# Objetivo

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário(cliente)
e cadastrar conta bancária

## desafio

Precisamos deixar o nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, 
depositar e visualizar histórico. Além disso, para versão 2 do nosso sistema precisamos criar duas novas funções: criar 
usuário(cliente do banco) e criar conta-corrente(vincular com o usuario)

## Separação em funções

Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função
vai ter uma regra de passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma
como achar melhor.

## Saque

A função deve receber os argumentos apenas por nome(keyword only). Sugestão de argumentos: Saldo, valor, Extrato, limite
numero_saque, limite_saques. Sugestão de retorno: saldo e extrato.

## Deposito

A função depósito deve receber os argumentos apenas por posição(positional only). Sugestão de argumentos: saldo, valor, 
extrato. Sugestão de retorno: saldo e extrato


## Extrato

A função extrato deve receber os argumentos por posição e nome (keyword only e positional only). Argumentos posicionais: 
saldo, argumento nomeado: extrato 

### novas funções

Precisamos criar duas novas funções: criar usuário e criar conta-corrente. Fique a vontade para adicionar mais funções, 
exemplo: listar contas.

## criar usuário(cliente)
O programa deve armazenar os usuários numa lista, um usuário é composto por: nome, data de nascimento, cpf e endereço.
O endereço é uma String com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somente os 
números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF. 

## criar conta corrente

O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário. O número da
conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuario pode ter mais de uma conta, mas uma 
conta pertence a somente 1 usuario

## Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário 
da lista.