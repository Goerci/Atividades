import datetime

hoje = datetime.datetime.now()

# Pessoa 1
nome1 = input("Nome da primeira pessoa: ")
data_str1 = input("Data de nascimento (dd/mm/aaaa): ")
data1 = datetime.datetime.strptime(data_str1, "%d/%m/%Y")

# Pessoa 2
nome2 = input("Nome da segunda pessoa: ")
data_str2 = input("Data de nascimento (dd/mm/aaaa): ")
data2 = datetime.datetime.strptime(data_str2, "%d/%m/%Y")

# Cria a data do aniversário de cada um para este ano
aniv1 = datetime.datetime(hoje.year, data1.month, data1.day)
aniv2 = datetime.datetime(hoje.year, data2.month, data2.day)

# Se o aniversário já passou este ano, calculamos a distância para o próximo ano
if aniv1 < hoje:
    aniv1 = datetime.datetime(hoje.year + 1, data1.month, data1.day)
if aniv2 < hoje:
    aniv2 = datetime.datetime(hoje.year + 1, data2.month, data2.day)

# Calcula a quantidade de dias que faltam
dias_p1 = (aniv1 - hoje).days
dias_p2 = (aniv2 - hoje).days

# Compara quem está mais perto
if dias_p1 < dias_p2:
    print(f"\nO aniversário de {nome1} está mais próximo (faltam {dias_p1} dias).")
elif dias_p2 < dias_p1:
    print(f"\nO aniversário de {nome2} está mais próximo (faltam {dias_p2} dias).")
else:
    print("\nAmbos os aniversários estão à mesma distância de dias!")