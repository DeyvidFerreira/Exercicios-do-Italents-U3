import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# Inicio
Info_aluno = {
    "nome": "",
    "media": 0.00,
    "situacao": "",
}

# entrada
print("Bem vindo ao sistema da escola\n")
nome = input("Por favor digite o nome do aluno: ")
media = input("Agora digite a média do aluno: ")
clear()

# alguns calculos
Info_aluno["nome"] = nome
media = float(media)
Info_aluno["media"] = media

if media >= 7 and media <= 10:
    Info_aluno["situacao"] = "O aluno foi aprovado."
elif media >= 5:
    Info_aluno["situacao"] = "O aluno está em recuperação."
else:
    Info_aluno["situacao"] = "O aluno foi reprovado."

# Saída
print("Aluno: ",Info_aluno["nome"],"\nMédia do aluno: ",Info_aluno["media"],"\nSituação: ",Info_aluno["situacao"])