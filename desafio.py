CONSTANTE_BONUS = 1000

# 1. Solicita ao usuário que digite seu nome.
try:
    nome_usuario = input("Digite o seu nome: ")

    if nome_usuario.isdigit():
        raise ValueError("Você digitou seu nome errado!")

    elif len(nome_usuario) == 0:
        raise ValueError("Você não digitou nada!")

except ValueError as e:
    print(f"Erro: {e}")
    exit()

# 2. Solicita ao usuário que digite o valor do seu salário.
# Converte a entrada para um número de ponto flutuante

try:
    salario = float(input("Digite o valor do salario: "))

    if salario <= 0:
        raise ValueError("Salário tem que ser positivo!")

except ValueError:
    print("Entrada inválida, Por favor digite só números!")
    exit()


# 3. Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    bonus = float(input("Digite o valor do bônus: "))

    if bonus <= 0:
        raise ValueError("Bônus tem que ser positivo!")
    
except ValueError:
    print("Entrada inválida, Por favor digite apenas números")
    exit()

# 4. Calcule o valor do bônus final 

valor_do_bonus = round((CONSTANTE_BONUS + salario * bonus),2)


# 5. Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus.

print(f"O usuário {nome_usuario} possui um bônus de R${valor_do_bonus} reais.")


