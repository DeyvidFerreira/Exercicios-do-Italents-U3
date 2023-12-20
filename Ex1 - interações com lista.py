import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(segunds):
    time.sleep(segunds)

clear()

# Inicio do código
lista = [5, 7, 9, 4, 1, 3]

print("A quantidade de elementos na lista é ", len(lista))

# o maior numero da lista
maior = 0
for i in lista:
    if maior < i:
        maior = i

menor = maior
for x in lista:
    if menor > x:
        menor = x

print(f"O maior numero na lista é {maior}\nE o menor é {menor}")

# Soma de todos os numeros da lista
res_soma = sum(lista)
print("A soma de todos os elementos da lista é: ",res_soma)

# Lista em ordem crecente e decrecente
lista_crecente = sorted(lista)
lista_decrecente = lista_crecente[::-1]

print("A lista de forma crecente: ",lista_crecente,"\n E de forma decrecente é: ",lista_decrecente)