import os

while True:
    print("Vamos calcular os lados do triângulo retântugulo e sua área")
    opcao = input("Para descobrir a hipotenusa, digite H, para um dos catetos digite C: ")
    opcao = opcao.upper()

    if opcao == "C":
        hipostr = input("Digite o valor da hipotenusa: ")
        cateto1str = input("Digite o valor do cateto: ")
        
        try:
            hipo = float(hipostr)
            cateto1 = float(cateto1str)
            validador = True
        except:
            validador = None
        
        if validador is None:
            print('Você não digitou um número válido!')
            continue

        cateto2 = (((hipo*hipo)-(cateto1*cateto1))**(1/2))
        os.system('cls')
        print(f'O valor do outro cateto é: {cateto2}')
        area = (cateto1*cateto2)/2
        print(f'A área do triângulo é: {area}')

    elif opcao == "H":
        cateto1str = int(input("Digite o valor do cateto: "))
        cateto2str = int(input("Digite o valor do outro cateto: "))

        try:
            cateto1 = float(cateto1str)
            cateto2 = float(cateto2str)
            validador = True
        except:
            validador = None
        if validador is None:
            print('Você não digitou um número válido!')
            os.system('cls')
            continue

        hipo = ((cateto1*cateto1)+(cateto2*cateto2))**(1/2)
        os.system('cls')
        print(f'O valor da Hipotenusa é: {hipo}')
        area = (cateto1*cateto2)/2
        print(f'A área do triângulo é: {area}')

    else:
        os.system('cls')
        print("Você não digitou uma opção válidaa")
    
    continue