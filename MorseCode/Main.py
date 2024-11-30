def traducao_alfabeto(AlfabetoeNumero, morse, mensagem):
    i = 0
    indices = len(mensagem) #coleta o numero total de indices de mensagem
    traduzida = [None] * indices  # cria um vetor com a mesma quantidade de indices de mensagem, mas com os valores nulos

    while i < indices:
        letra = AlfabetoeNumero.index(str(mensagem[i]))  # letra é igual ao indice do elemento em alfabeto correspondente ao elemeto i de mensagem
        traduzida[i] = morse[letra] #substitui o indice i de traduzida para o correspondente ao indice com valor obtido em letra dentro de morse
        i += 1

    return traduzida

def traducao_morse(AlfabetoeNumero, morse, msg):
    i = 0
    indices = len(msg) #coleta o numero total de indices de msg
    traduzida = [None] * indices  # cria um vetor com a mesma quantidade de indices de mensagem, mas com os valores nulos

    while i < indices:
        letra = morse.index(msg[i]) # letra é igual ao indice do elemento em morse correspondente ao elemeto i de mensagem
        traduzida[i] = AlfabetoeNumero[letra] #substitui o indice i de traduzida para o correspondente ao indice com valor obtido em letra dentro de AlfabetoeNumero
        i += 1

    return traduzida

def traducao(mensagem, msg):
    AlfabetoeNumero = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "/", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    if mensagem[0] in AlfabetoeNumero:
        traduzida = traducao_alfabeto(AlfabetoeNumero, morse, mensagem)
        traduzida = " ".join(traduzida) #define traduzida como um str de traducao_alfabeto.traduzida dando espaço a cada indice
    else:
        traduzida = traducao_morse(AlfabetoeNumero, morse, msg)
        traduzida = "".join(traduzida) #define traduzida como um str de traducao_alfabeto.traduzida sem espaço a cada indice


    print(traduzida)

mensagem = input("Insira a mensagem ou codigo a ser traduzido: ")
msg = mensagem.split() #cria um vetor de mensagem

traducao(mensagem, msg)