import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# inicio
pontuacao_Sus = []

def resposta(afirmação):
    if afirmação in ["postivo", "sim", "si", "yes", "s"]:
        pontuacao_Sus.append(1)
    elif afirmação in ["negativo","nao", "não", "no", "not", "n", "sus"]:
        pontuacao_Sus.append(0)
    else:
        pontuacao_Sus.append(6 * 10 ** 23) # Para respostas claramente de um impostor
    clear()

print("Boa tarde, vamos fazer umas perguntas sobre um dia, tudo bem?\nPor favor responda as perguntas com s ou sim para postivo, n ou não para negação")

resposta(input("Nesse dia você, telefonou para essa pessoa?\n"))
resposta(input("Você esteve nesse lugar?\n"))
resposta(input("Tu mora perto dessa pessoa?\n"))
resposta(input("Tu é caloteiro? tava devendo pix para ele?\n"))
resposta(input("Tu ja trabalhou junto com a pessoa?\n"))

pontos = sum(pontuacao_Sus)

if pontos < 2:
    sus_index = "Inocente"
elif pontos == 2:
    sus_index = "Suspeito"
elif pontos in [3, 4]:
    sus_index = "Cumplice"
elif pontos == 5:
    sus_index = "Assasino"
else:
    sus_index = "Impostor"

print("Você claramente é um ",sus_index,", você tirou uma pontuação de ",pontos," Na pesquisa")