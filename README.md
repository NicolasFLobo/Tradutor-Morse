# Tradutor-Morse

O codigo é um desafio de programação no qual deve-se criar um programa para traduzir uma mensagem em morse para o alfabeto latino/alfabeto latino para morse

#Funcionamento

O codigo é de um funcionamento simples:

1. **Entrada de dados**:
   A entrada de dados é por meio de uma variavel mensagem que recebe um input str e uma variavel msg que recebe mensagem com .split() e se torna um vetor

2. **Processamento**:
     Ao definir as duas variaveis, é chamada a função traducao(). Dentro de traducao() estão definidos dois vetores, referentes ao alfabeto latino e ao morse, logo após é usado uma condicional para verificar se o primeiro caracter da variavel x está contido     no vetor AlfabetoeNumero, é assim que o programa determina se a tradução é de alfabeto latino para morse ou morse para latino.
     Caso a condicional seja verdadeira, o programa faz a chamada da função traducao_alfabeto() atribuida a uma variavel traduzida. Caso contrario, ele faz a chamada da função traducao_morse() atribuinda a uma mesma variavel traduzida.
     O funcionamento de traducao_alfabeto() e traducao_morse() são o mesmo, o que muda é apenas de qual vetor ele vai retirar o    caracter ao fazer a tradução. Dentro das funções, ele define dentro do escopo a variavel traduzida como um vetor com o indice, de valor nulo, igual ao numero total de letras da variavel mensagem ou do indice da variavel msg, apos isso, usa-se um laço de repetição for para percorrer cada letra ou indice das suas respectiva variavel.
     Dentro do for a variavel letra é um numero inteiro igual a posição que a letra ou indice ocupam dentro dos vetores AlfabetoeNumero ou Morse, por fim os indices da variavel traduzida são substituidos de nulo para o valor correspondente a letra dentro dos respectivos vetores e é retornada.

2. **Saida de dados**:
     De volta a função traducao, traduzida recebe o retorno das respectivas funções chamadas e torna-se um vetor. Por fim, traduzida é revertida em uma str, caso a tradução feita tenha sido do alfabeto latino para morse, é adicionado um espaço entre cada indice ao serem revertidos, caso contrario, não há espaços entre cada indice (Ex: ['a', 'b', 'c'] -> '.- -... -.-.' ou ['.-', '-...', '-.-.'] -> "abc"), após isso é feito um print da variavel traduzida.

#Como rodar o programa

Para rodar o programa basta possuir uma IDE python e clonar o repositorio em sua maquina, recomenda-se o uso da IDE pycharm.
