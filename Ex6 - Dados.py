import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# Inicio
clientes = [
    {
        "nome": "joão",
        "idade": 18,
        "genero": "M",
    },
    {
        "nome": "Maria",
        "idade": 50,
        "genero": "F",
    },
    {
        "nome": "Shaollin",
        "idade": 15,
        "genero": "M",
    },
    {
        "nome": "Jeniffer",
        "idade": 17,
        "genero": "F",
    },
    {
        "nome": "Flavinho do Pneu",
        "idade": 120,
        "genero": "M",
    }
]

responsavel = []
menor = []

for dados in clientes:
    nome = dados["nome"]
    idade = dados["idade"]

    if idade >= 18:
        responsavel.append(nome)
    else:
        menor.append(nome)

# Saida
for i in responsavel:
    print({i}," é maior de idade;")

print("A ",len(responsavel)," usuários maiores de idade.\n")

for a in responsavel:
    print({a}," é menor de idade;")

print("A ",len(menor)," usuários menores de idade.")
