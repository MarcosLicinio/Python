import os
valido = True
listadecompras = []
opcaodecompra = ''
delete = ''

while valido:
    print('- - Bem vindo ao programa que cria uma lista de compras - -')
    print('\t\t[I]nserir')
    print('\t\t[D]eletar')
    print('\t\t[L]istar')
    print(' ')

    opcao = input('Digite a opção desejada: ')
    opcao = opcao.upper()

    if opcao == 'I':
        os.system('cls')
        listadecompras.append(input('Digite um produto para inserir na lista: ')) #adiciona item na lista
        continue

    elif opcao == 'D':
        os.system('cls')
        if listadecompras == '':
            print('Sua lista está vazia!')
            continue
        print('Sua lista de compras é:')
        for i, produto in enumerate(listadecompras, start=1): #função para mostrar lista enumerada 
            print(i, produto)

            continue

        delete = int(input('Digite o numero do produto acima você deseja deletar? '))
        if delete >= 0 and delete <= len(listadecompras):
            listadecompras.pop(delete - 1) #exclui item da lista
            os.system('cls')
        else:
            print('Você digitou um numero que não corresponde a nenhum produto')
            os.system('cls')
            continue
        continue

    elif opcao == 'L':
        os.system('cls')
        print('Sua lista de compras é:')
        for i, produto in enumerate(listadecompras, start=1): #função para mostrar lista enumerada 
            print(i, produto)
            continue

    else:
        os.system('cls')
        print('Você digitou uma opção inválida')
        continue 
