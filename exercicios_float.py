
# 1 - Escreva um programa que receba dois números flutuantes e realize sua adição.
print ("1 - Escreva um programa que receba dois números flutuantes e realize sua adição.")

primeiro = float(input("Digite o primeiro número de sua preferência: "))
segundo = float(input("Digite o segundo número de sua preferência: "))

resultado = primeiro + segundo

print (f'O resultado da soma é: {resultado}')
# 2 -  Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print ("2 -  Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.")

primeiro = float (input ("Digite o primeiro número de sua preferência: "))
segundo = float(input("Digite o segundo número de sua preferência: "))
média = 2

resultado_media =  (primeiro + segundo) / média

print (f'A média é: {resultado_media}')
# 3 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
print ("3 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário)")

base = float (input("Digite o primeiro número de sua preferência: "))
expoente = float (input ("Digite o segundo número de sua preferência: "))

resultado_potencia = base ** expoente

print (f'Resultado da potência é: {resultado_potencia}')

# 4 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.
print ("4 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.")

celsius = float (input("Digite a temperatura para conversão: "))
conversao_1 = 1.8
conversao_2 = 32

resultado_conversao = (celsius * conversao_1) + conversao_2

print (f'Resultado da conversão para Fahrenheit é: {resultado_conversao}°')


# 5 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print ("5 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.")

raio = float(input ("Digite o raio do circulo: "))**2
pi = 3.14

resultado_area = pi * raio

print (f'O resultado da área é: {resultado_area}')