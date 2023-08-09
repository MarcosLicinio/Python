print("Bem vindo ao cálculo de Bhaskara, vamos resolver a equação de segundo grau")
print("Ela deve estar no seguinte formato: ax^2 + bx + c = 0")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = ((b*b)-(4*a*c))
if delta > 0:
    print(f'O valor do Delta é: {delta} , neste caso a equação terá dois valores reais e distintos')
elif delta == 0:
    print(f'O valor do Delta é: {delta} , neste caso a equação terá apenas um valor real ou dois resultados iguais')
elif delta < 0:
    print(f'O valor do Delta é: {delta} , neste caso a equação não terá valores reais')
else:
    print("Você não digitou valores corretos")

x1 = ((-1*b)-(delta**(1/2)))/(2*a)

x2 = ((-1*b)+(delta**(1/2)))/(2*a)

print(f' O valor de x1 é: {x1}')
print(f' O valor de x2 é: {x2}')