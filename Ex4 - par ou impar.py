import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# Inicio do meu código
banco = []
banco_filtrado = [
    [],
    []
]

# entrada
print("Bem vindo ao banco de dados de numeros,\nDigite um numero inteiro ou escreva sair para encerrar:")
while True:
    entrada = input()

    if entrada.lower() ==  "sair":
        break
    
    try:
        numero = int(entrada)
        if not numero in banco:
            banco.append(numero)
        else:
            print("Por favor, Não repita o mesmo numero.")
    except ValueError:
        print("Por favor, digite um numero válido.")
    
clear()

# Primeira lista
banco.sort()
print("Os numeros digitados de forma crecente é ",banco)

# Separação dos numeros
for i in banco:
    elemento = i
    if elemento % 2 == 0:
        banco_filtrado[0].append(elemento)
    else:
        banco_filtrado[1].append(elemento)

print(f"O mesmo numeros apenas pares, ficaria assim: {banco_filtrado[0]}")
print(f"O mesmo numeros apenas impares, ficaria assim: {banco_filtrado[1]}")