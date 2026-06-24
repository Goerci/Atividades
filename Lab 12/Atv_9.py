import datetime

# Obtém a data atual
hoje = datetime.datetime.now()

# Define a data da prova (Ano, Mês, Dia)
data_prova = datetime.datetime(2026, 7, 14)

# Calcula a diferença (Data futura - Data atual)
diferenca = data_prova - hoje

# Exibe a quantidade de dias restantes
print(f"Faltam exatamente {diferenca.days} dias para a sua prova!")