morseCaracteres = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
          'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
          's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
          '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
          '7': '--...', '8': '---..', '9': '----.'}

print('O Programa ira traduzir para codigo morse uma mensagem do usuario.')
mensagem = input('Digite sua mensagem: ')

caracteres = []
for x in range(len(mensagem)):
    caractere = mensagem[x].lower()
    if caractere in morseCaracteres.keys():
        caracteres.append(caractere)

morse = list(map(lambda c: morseCaracteres[c], caracteres))
mensagemTraduzida = ' '.join(morse)
print(f'Sua mensagem em Código Morse é:\n{mensagemTraduzida}')