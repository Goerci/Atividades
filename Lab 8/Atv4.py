num = 0
while num < 100:
    escolha = int(input("Digite um numero postivo: "))
    if escolha < 0:
        print("Apenas numeros positivos!!")
        continue
    elif escolha == 0:
        break
    else:
        num += escolha