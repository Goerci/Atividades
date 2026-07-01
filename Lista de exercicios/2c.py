import datetime

hoje = datetime.datetime.now()

ano = int(input("Que ano você nasceu?"))

print(hoje.year, ano, hoje.year - ano)

#Entrada: 1987 Saída: 2025 1987 38

#Entrada: 2000 Saída: 2025 2000 25

#Entrada: 2011 Saída: 2025 2011 14