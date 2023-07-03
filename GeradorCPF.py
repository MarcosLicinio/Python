import random

novedigitos = ''
print('Gerador de CPF: ')
for i in range(9):
    novedigitos += str(random.randint(0, 9))

contadoregressivo1 = 10
resultadodigito1 = 0

for digito in novedigitos:
    resultadodigito1 += int(digito) * contadoregressivo1
    contadoregressivo1 -= 1

digito1 = (resultadodigito1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

dezdigitos = novedigitos + str(digito1)

contadoregressivo2 = 11
resultadodigito2 = 0

for digito in dezdigitos:
    resultadodigito2 += int(digito) * contadoregressivo2
    contadoregressivo2 -= 1
digito2 = (resultadodigito2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpfgerado = str(f'{novedigitos}{digito1}{digito2}')

cpf = cpfgerado[:3] + '.' + cpfgerado[3:6] + '.' + cpfgerado[6:9] + '-' + cpfgerado[9:]

print(cpf)