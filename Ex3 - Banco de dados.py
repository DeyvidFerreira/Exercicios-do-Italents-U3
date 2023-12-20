import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# Inicio do meu código
banco = []

print("Bem vindo ao banco de dados de numeros,\nDigite um numero ou escreva sair para encerrar:")
while True:
    entrada = input()

    if entrada.lower() ==  "sair":
        break
    
    try:
        numero = float(entrada)
        if not numero in banco:
            banco.append(numero)
        else:
            print("Por favor, Não repita o mesmo numero.")
    except ValueError:
        print("Por favor, digite um numero válido.")
    
clear()

banco.sort()
print("Os numeros digitados de forma crecente é ",banco)