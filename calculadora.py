while True:
    print('- - Calculadora - -')
    n1 = (input('Digite o primeiro valor: '))
    n2 = (input('Digite o segundo valor: '))
    numerovalido = None

    try:
        n1float = float(n1)
        n2float = float(n2)
        numerovalido = True
    except:
        numerovalido = None
    
    if numerovalido is None:
        print('Você não digitou um número válido!')
        continue

    print('(1) para somar ( + )')
    print('(2) para subtrair ( - )')
    print('(3) para multiplicar ( * )')
    print('(4) para dividir ( / )')

    operacao = input('Opção desejada: ')


    if operacao == '1':
        print('O valor é: ', n1float + n2float)
    elif operacao == '2':
        print('O valor é: ', n1float - n2float)
    elif operacao == '3':
        print('O valor é: ', n1float * n2float)
    elif operacao == '4':
        print('O valor é: ', n1float / n2float)
    else:
        print('Operação matemática não encontrada')
        continue

    sair = input('Você deseja sair? [S]im [N]ao] ').lower().startswith('s')
    if sair is True:
        break