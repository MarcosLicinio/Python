print('Vamos descobrir os 2 ultimos números do seu CPF')
cpf_digitado = input('Digite os 9 primeiros números do seu CPF: ')
caracteres = '.,-'

for i in range(0,len(caracteres)): #retira os caracteres ,.- do número do CPF
    cpf_digitado = cpf_digitado.replace(caracteres[i], '')

d0_1 = int(cpf_digitado[0]) * 10
d1_1 = int(cpf_digitado[1]) * 9
d2_1 = int(cpf_digitado[2]) * 8
d3_1 = int(cpf_digitado[3]) * 7
d4_1 = int(cpf_digitado[4]) * 6
d5_1 = int(cpf_digitado[5]) * 5
d6_1 = int(cpf_digitado[6]) * 4
d7_1 = int(cpf_digitado[7]) * 3
d8_1 = int(cpf_digitado[8]) * 2

somadigitos1 = ((d0_1 + d1_1 + d2_1 + d3_1 + d4_1 + d5_1 + d6_1 + d7_1 + d8_1) * 10)

sobra = somadigitos1 % 11

decimodigito = sobra if sobra <= 9 else 0

cpf_digitado = cpf_digitado + str(decimodigito)

d0_2 = int(cpf_digitado[0]) * 11
d1_2 = int(cpf_digitado[1]) * 10
d2_2 = int(cpf_digitado[2]) * 9
d3_2 = int(cpf_digitado[3]) * 8
d4_2 = int(cpf_digitado[4]) * 7
d5_2 = int(cpf_digitado[5]) * 6
d6_2 = int(cpf_digitado[6]) * 5
d7_2 = int(cpf_digitado[7]) * 4
d8_2 = int(cpf_digitado[8]) * 3
d9_2 = int(cpf_digitado[9]) * 2

somadigitos2 = ((d0_2 + d1_2 + d2_2 + d3_2 + d4_2 + d5_2 + d6_2 + d7_2 + d8_2 + d9_2) * 10)

sobra2 = somadigitos2 % 11

decimoprimeirodigito = sobra2 if sobra2 <= 9 else 0

novocpf = cpf_digitado + str(decimoprimeirodigito)
print(f'Os dois ultimos dígitos do seu CPF é: {decimodigito}{decimoprimeirodigito}')

print(f'O CPF completo é: {novocpf}')