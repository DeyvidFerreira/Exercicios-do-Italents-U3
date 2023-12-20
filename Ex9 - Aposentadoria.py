import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

def input_number(text,error="Não entendi, tente novamente.",inteiro=False):
    while True:
        try:
            entrada = input(text)
            number = float(entrada)
            if inteiro:
                number = int(number)
            elif number % 1 == 0:
                number = int(number)
            return(number)
        except ValueError:
            clear()
            print(error)

# Inicio
pessoa = {}
aposentadoria_min_idade = 35
ano_atual = 2023

# Entrada
nome = input("Qual é o seu nome: ")
nacimento = input("Qual é sua data de nacimento: ")
ctps = input_number("Qual é o numero da sua carteira de trabalho: ","Não entendi, tente usar apenas numeros, sem espaço",True)
clear()

pessoa = {"nome": nome,"data": nacimento,"ctps":ctps}
if pessoa["ctps"] != 0:
    contratacao = input_number("Qual foi seu ano de Contratação: ","Tente coloca nesse formato yyyy",True)
    salario = input_number("Qual é o seu Salário: R$")
    aposentadoria = aposentadoria_min_idade - (ano_atual - contratacao) + ano_atual
    clear()

    pessoa.update({"contratação": contratacao, "Salário": salario, "aposentadoria": aposentadoria})

    print("Informações:")
    for i, valor in pessoa.items():
        print(f"{i}: {valor}")
else:
    print("Erro")