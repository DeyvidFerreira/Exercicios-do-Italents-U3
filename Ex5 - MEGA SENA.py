import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def chut(min, max):
    return random.randint(min, max)

clear()

# Inicio
matrix = []

def jogar(vezes):
    for n in range(1,vezes + 1):
        soteado = []

        for i in range(1, 7):
            soteado.append(chut(1, 60))
        
        matrix.append(soteado)

# Entrada
print("Por favor digite a quantidade de jogos da Mega Sena: ")
while True:
    try:
        numero = int(input())
        break
    except ValueError:
        print ("Tente dizer um numero inteiro")

jogar(numero)
clear()

# Saída
print("Os numeros sorteados são: \n")

for linha in matrix:
    print(linha)