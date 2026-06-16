respostas_n = "n", "N", "Não", "não"
respostas_s = "s", "S","sim", "Sim"
while True:
    batata = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N: ")
    if batata == 's' or batata == "S":
        continue 
    elif batata == 'n' or batata == 'N':
        break 
    else:
        print("Não é uma resposta valida")
        continue