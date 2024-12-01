# Tradutor_Morse

O codigo é um desafio de programação no qual deve-se criar um programa para traduzir uma mensagem em morse para o alfabeto latino/alfabeto latino para morse.

# Funcionamento

O codigo é de um funcionamento simples:

**Entrada de dados**:

   A entrada de dados é por meio de uma variavel mensagem que recebe um input str e uma variavel msg que recebe mensagem com .split() e se torna um vetor.

**Processamento**:

   Ao definir as duas variaveis, é chamada a função traducao(). Dentro de traducao() estão definidos dois vetores, referentes ao alfabeto latino e ao morse. Logo após, é usada uma condicional para verificar se o primeiro caracter da variavel x está contido no vetor AlfabetoeNumero. É assim que o programa determina se a tradução é de alfabeto latino para morse ou de morse para latino.
   
   Caso a condicional seja verdadeira, o programa faz a chamada da função traducao_alfabeto() atribuída a uma variavel traduzida.  Caso contrario, ele faz a chamada da função traducao_morse() atribuida à mesma variavel traduzida.
   O funcionamento de traducao_alfabeto() e traducao_morse() é o mesmo. O que muda é apenas de qual vetor ele vai retirar o caracter ao fazer a tradução. Dentro das funções, ele define dentro do escopo a variavel traduzida como um vetor com o indice, de valor nulo, igual ao numero total de letras da variavel mensagem ou do indice da variavel msg. Apos isso, usa-se um laço de repetição for para percorrer cada letra ou indice das respectivas variaveis.
   
   Dentro do laço for, a variavel letra é um numero inteiro igual à posição que a letra ou indice ocupa dentro dos vetores AlfabetoeNumero ou Morse. Por fim, os indices da variavel traduzida são substituídos de nulo para o valor correspondente à letra dentro dos respectivos vetores, e a variavel é retornada.

**Saida de dados**:

   De volta à função traducao, traduzida recebe o retorno das respectivas funções chamadas e torna-se um vetor. Por fim, traduzida é revertida em uma str. Caso a tradução feita tenha sido do alfabeto latino para morse, é adicionado um espaço entre cada indice ao serem revertidos. Caso contrario, não há espaços entre cada indice (Ex: ['a', 'b', 'c'] -> '.- -... -.-.' ou ['.-', '-...', '-.-.'] -> "abc"). Após isso, é feito um print da variavel traduzida.

# Como rodar o programa

Para rodar o programa basta possuir uma IDE python e clonar o repositorio em sua maquina. Recomenda-se o uso da IDE pycharm.
