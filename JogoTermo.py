import os
caracter = '*'
letrasacertadas = ''
contador = 0
opcoesescolhidas = ''
lista = ['carro', 'casa', 'boneca', 'perfume', 'janela', 'sofá', 'montanha', 'nuvem', 'cavalo', 'mesa']

while True: 

    print('- - Bem vindo ao jogo TERMO versão Pythoresca - -')
    opcao_escolhida = input('Digite de 1 a 10 para escolher uma palavra secreta: ')

    if opcao_escolhida in opcoesescolhidas:
        print('Você já escolheu esta palavra')
        continue

    palavrasecreta = lista[(int(opcao_escolhida) - 1)]
    opcoesescolhidas += opcao_escolhida

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
            os.system('cls')
            print('Parabéns! Você acertou a palavra!')
            letradigitada = ''
            palavraacertada = ''
            letrasacertadas = ''
            contador = 0
            break

        if contador >= 10:
            os.system('cls')
            print('Você atingiu o máximo de tentativas, o jogo será reiniciado')
            letradigitada = ''
            palavraacertada = ''
            letrasacertadas = ''
            contador = 0
            break
