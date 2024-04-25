Fomos contratado por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar
suas operações e para isso escolheu a linguagem ptython. Para a
primeira versão do sistema devemos implementar apenas 3 operações: depoósito, saque e extrato

Depósito:
Deve ser possivel despositar valores positivos para a minha conta bancária.
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos
nos preocupar em identificar qual é o número da agência e conta bancária.
Todos os depósitos devem ser armazenados em uma variável e exibiddos na
operação extrato

Saque:

O sistema deve permitir realizar 3 saques diarios com limite máximo de
R$500,00 por saque. caso o usuário não tenha saldo em conta, o sistema
deve exibir uma mensagem informando que não será possível sacar o dinheiro
por falta de saldo. Todos os saques devem ser amarzenados em uma variável
e exibidos na operação extrato

Extrato:
Essa operação deve listar todos os depósitos e saques realizados na conta.
No dim da listagem deve ser exibido o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx. exemplo

1500,45 = R$1500.45