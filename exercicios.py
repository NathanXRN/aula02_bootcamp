import math
import re

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

# 21. Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e,
# utilizando `try-except`, garantir que a entrada seja numérica, tratando qualquer ValueError.
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    temperatura_celsius = float(input("Digite a temperatura em Graus Celsius: "))
    temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32
    print(temperatura_fahrenheit)
except:
    print("invalid number! Try again...")

# 22. Crie um programa que verifica se uma palavra ou frase é um palíndromo. Utilize `try-except` para garantir que a entrada seja uma string.
# Dica: Utilize a função isinstance() para verificar o tipo de entrada.

def palindromo(frase):
    frase_normal = frase.lower()
    frase_normal = re.sub(r'[^a-z]', '', frase_normal)
    frase_invertida = frase_normal[::-1]
    return frase_normal == frase_invertida


try:
    frase = input("Digite uma frase: ")
    if isinstance(frase, str):
        if re.search(r'[0-9]', frase):
            raise ValueError("Números não são permitidos")
        if palindromo(frase):
            print("É palíndromo")
        else:
            print("Não é palíndromo")
except Exception as err:
    print("Invalid Value! Please, try again!")

# 23. Calculadora Simples 
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador(+,-,*,/) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas.
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou manda uma mensagem de erro apropriada.
try:
    num1     = float(input("Digite um número: "))
    num2     = float(input("Digite outro número: "))
    
    operador = input("Digite o operador: ")

    if operador not in ['+','-','*','/']:
        raise ValueError("Operador Inválido")
    
    if operador == '+':
        resultado = num1 + num2 
        print(f"{num1} + {num2} = {resultado}")

    elif operador == '-':
        resultado = num1 - num2 
        print(f"{num1} - {num2} = {resultado}")

    elif operador == '*':
        resultado = num1 * num2 
        print(f"{num1} * {num2} = {resultado}")

    elif operador == '/':
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida")
        resultado = num1 / num2 
        print(f"{num1} / {num2} = {resultado}")

except ValueError as e:
    if "Não foi possível converter" in str(e):
        print("Erro: Digite apenas números válidos!")
    else:
        print(f"Erro:{e}")

except ZeroDivisionError as e:
    print(f"Erro: {e}")

except Exception as e:
    print("Erro inesperado! Tente novamente")

# 24. Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar
# o número como "positivo", "negativo", ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

def classificador():
    """Classificador de Números com tratamento de erros"""
    try:
        print("===CLASSIFICADOR DE NÚMEROS===")

        num = float(input("Digite um número: "))

        if num == 0:
            print(f"{num} = ZERO ")
        
        elif num > 0:
            print(f"{num} = POSITIVO ")
        
        else:
            print(f"{num} = Negativo ")
        
        if num % 2 == 0:
            print(f"Este número {num} é par!")
        
        else:
            print(f"Este número {num} é ímpar!")
        
    except ValueError as e:
        if "could not convert" in str(e):
            print("Digite apenas números!")
        else:
            print(f"Erro: {e}")

    except Exception as e:
        print("Erro Inesperado, Tente Novamente!")

classificador()

# 25. Conversão do Tipo com Validação 
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros.
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um
# inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

def conversao_lista():
    """Conversão do Tipo com Validação e com tratameno de erros"""
    
    try:
        print("===Conversão do Tipo com Validação===")

        lista_numeros = []

        entrada = input("Digite números separados por vírgulas: ")

        numero_str = entrada.split(",")

        for i, numero_str in enumerate(numero_str):
            try:
                numero = int(numero_str.strip())
                lista_numeros.append(numero)

            except ValueError:
                raise ValueError(f"Erro na posição {i+1}: '{numero_str.strip()}' não é um número válido!")
            
        print(f"Conversão bem-sucedida!")
        print(f"lista_numeros = {lista_numeros}")

    except ValueError as e:
        print(f"Erro de conversão: {e}")

    except Exception as e:
        print(f"Erro inesperado: {e}")

conversao_lista()




    
    