# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário
print ("1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário")
primeiro = int(input("Digite o primeiro número: "))


segundo = int(input("Digite o segundo número: "))


soma = int(primeiro + segundo)

print (f'A soma dos valores digitados é: {soma}')



# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print ("2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5")
primeiro = int (input("Digite o primeiro número desejado: "))

segundo = int (input("Digite o segundo número desejado: "))

resultado_resto = primeiro % segundo
print (f'O resto da divisão é: {resultado_resto}')

resultado = resultado_resto * 5

print (f'O resultado da conta é: {resultado}' )

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print ("3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado")
primeiro = int (input("Digite o primeiro número desejado: "))

segundo = int (input("Digite o segundo número desejado: "))

resultado_multiplicacao = primeiro * segundo

print (f'Resultado da multiplicação é: {resultado_multiplicacao}')


# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print ("4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.")
primeiro = int (input("Digite o primeiro número desejado: "))

segundo = int (input("Digite o segundo número desejado: "))

resultado_divisao = primeiro // segundo

print (f'Resultado da divisão é: {resultado_divisao}')



# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

print ("5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.")
primeiro = int (input("Digite o primeiro número desejado: "))

segundo = 2

resultado_potencia = primeiro ** segundo

print (f'Resultado da divisão é: {resultado_potencia}')
