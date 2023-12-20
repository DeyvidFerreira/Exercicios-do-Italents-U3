import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# Inicio
Produtos = [
    {
        "Nome": "Laranja",
        "Quantidade": 523,
    },
    {
        "Nome": "Iphone 21 pro max premium +",
        "Quantidade": 101,
    },
    {
        "Nome": "Pneu",
        "Quantidade": 0,
    },
    {
        "Nome": "Apartamento",
        "Quantidade": 45,
    },
]

print("Selecione o Produto da loja: \n")

cont = 0
for produto in Produtos:
    cont += 1
    print(f"[{cont}] {produto["Nome"]}")

# Verificação da escolha
while True:
    try:
        escolha = int(input("\nPor favor digite o código do produto: "))
        if escolha > 0 and escolha <= cont:
            escolha -= 1
            break
        else:
            print("Produto não encontrado tente novamente")
    except ValueError:
        print ("Codigo invalido, tente um numero inteiro da lista de produtos acima.")

clear()

# Verificação da quantidade escolhida e se tem no estoque
estoque = Produtos[escolha]["Quantidade"]

if estoque > 0:
    print("O produto está em estoque")

    while True:
        try:
            pedido = int(input("quantas unidades do produto vai querer?: "))

            if not pedido > estoque:
                print("A Quantidade escolhida está disponivel!")
            else:
                print("Desculpe mais a quantidade escolhida não está disponivel no estoque")

            break
        except ValueError:
            print ("Codigo invalido, tente um numero inteiro.")
else:
    print("Infelizmente o produto se encontra indisponivel.")
