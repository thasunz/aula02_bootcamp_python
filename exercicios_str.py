
# 1 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
digitacao = input ("Digite uma palavra ou frase: ")

print(f' Sua palavra ou frase em maiúscula é: {digitacao.upper()}')


# 2 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome em maiúsculo: ")

print (f'Seu nome em maiúsculo é: {nome.lower()}')



# 3 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input ("Digite uma frase: ")

print (f'Sua frase sem espaços em branco é {frase.strip()}')

# 4 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.



# 5 - Escreva um programa que concatene duas strings fornecidas pelo usuário.
palavra = str(input ("Digite uma palavra: "))
palavra_2 = str(input ("Digite uma ourta palavra: "))

print (f'Suas palavras concatenadas são: {palavra + palavra_2}')