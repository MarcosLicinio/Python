palavrasecreta = 'carro'
caracter = '*'
letrasacertadas = ''
contador = 0
print('- - Bem vindo ao jogo TERMO versão Pythoresca - -')

while True:
    print(f'Você tem {(10 - contador)} tentativas')
    letradigitada = input('Digite uma letra: ')
    contador = contador + 1

    if len(letradigitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letradigitada in palavrasecreta:
        letrasacertadas += letradigitada
    
    palavraacertada = ''

    for letrasecreta in palavrasecreta:
        if letrasecreta in letrasacertadas:
            palavraacertada += letrasecreta
        else:
            palavraacertada += caracter
    
    print(palavraacertada)

    if palavrasecreta == palavraacertada:
        print('Parabéns! Você acertou a palavra!')
        letradigitada = ''
        palavraacertada = ''
        letrasacertadas = ''
        contador = 0
        print('Jogo reiniciado')

    if contador >= 10:
        print('Você atingiu o máximo de tentativas, o jogo será reiniciado')
        letradigitada = ''
        palavraacertada = ''
        letrasacertadas = ''
        contador = 0
        continue
