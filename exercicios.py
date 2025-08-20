import math

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

valor1 = int(input("Digite o valor1: "))
valor2 = int(input("Digite o valor2: "))

resultado = valor1 + valor2

print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por5.

valor = int(input("Digite um valor: "))

resultado = valor % 5

print(resultado)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

valor1 = int(input("Digite o valor1: "))
valor2 = int(input("Digite o valor2: "))

resultado = valor1 * valor2

print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

valor1 = int(input("Digite o valor1: "))
valor2 = int(input("Digite o valor2: "))

resultado = valor1 // valor2

print(resultado)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

valor = int(input("Digite um valor: "))

resultado = valor ** 2

print(resultado)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

valor1 = float(input("Digite o valor1: "))
valor2 = float(input("Digite o valor2: "))

resultado = valor1 + valor2

print(resultado)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

valor1 = float(input("Digite o valor1: "))
valor2 = float(input("Digite o valor2: "))

resultado = (valor1 + valor2) / 2

print(resultado)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecido pelo usuário)

valor1 = float(input("Digite o valor1: "))
valor2 = float(input("Digite o valor2: "))

resultado = valor1 ** valor2

print(resultado)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit

grau_celsius = float(input("Digite a temperatura do grau Celsius: "))

f = (grau_celsius * 1.8) + 32

print(f)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

raio = float(input("Digite o valor do raio: "))

a = raio * math.pi ** 2

print(a)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

nome = input("Digite um nome: ")

resultado = nome.upper()

print(resultado)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_completo = input("Digite seu nome completo: ")

resultado = nome_completo.lower()

print(resultado)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços.

frase = input("Digite uma frase: ")

resultado = frase.strip()

print(resultado)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, mês e ano.

data = input("Insira uma data no formato dd/mm/aaaa: ")

dia_mes_ano = data.split("/")

dia = dia_mes_ano[0]
mes = dia_mes_ano[1]
ano = dia_mes_ano[2]

print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

nome1 = input("Digite um nome1: ")
nome2 = input("Digite um nome2: ")

resultado = nome1 + nome2

print(resultado)

# 16. Escreva um programa que avlie duas expressões booleanas iseridas pelo usuário e retorne o resultado da operação AND entre elas.

valor1 = True
valor2 = False

resultado = valor1 and valor2

print(resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

resultado = valor1 or valor2

print(resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

resultado = not valor1

print(resultado) 

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguas.

resultado = valor1 == valor2

print(resultado)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

resultado = valor1 != valor2

print(resultado)