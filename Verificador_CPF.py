print('VVamos conferir se o seu CPF é válido')
cpf_digitado = input('Digite o seu CPF: ')
caracteres = '.,-'


for i in range(0,len(caracteres)): #retira os caracteres ,.- do número do CPF
    cpf = cpf.replace(caracteres[i], '')
cpf = cpf_digitado[:9]

d0_1 = int(cpf[0]) * 10
d1_1 = int(cpf[1]) * 9
d2_1 = int(cpf[2]) * 8
d3_1 = int(cpf[3]) * 7
d4_1 = int(cpf[4]) * 6
d5_1 = int(cpf[5]) * 5
d6_1 = int(cpf[6]) * 4
d7_1 = int(cpf[7]) * 3
d8_1 = int(cpf[8]) * 2

somadigitos1 = ((d0_1 + d1_1 + d2_1 + d3_1 + d4_1 + d5_1 + d6_1 + d7_1 + d8_1) * 10)

sobra = somadigitos1 % 11

decimodigito = sobra if sobra <= 9 else 0

cpf = cpf + str(decimodigito)

d0_2 = int(cpf[0]) * 11
d1_2 = int(cpf[1]) * 10
d2_2 = int(cpf[2]) * 9
d3_2 = int(cpf[3]) * 8
d4_2 = int(cpf[4]) * 7
d5_2 = int(cpf[5]) * 6
d6_2 = int(cpf[6]) * 5
d7_2 = int(cpf[7]) * 4
d8_2 = int(cpf[8]) * 3
d9_2 = int(cpf[9]) * 2

somadigitos2 = ((d0_2 + d1_2 + d2_2 + d3_2 + d4_2 + d5_2 + d6_2 + d7_2 + d8_2 + d9_2) * 10)

sobra2 = somadigitos2 % 11

decimoprimeirodigito = sobra2 if sobra2 <= 9 else 0

novocpf = cpf + str(decimoprimeirodigito)

if cpf_digitado == novocpf:
    print('O CPF digitado é válido!')
else:
    print('Você digitou um CPF inválido')
