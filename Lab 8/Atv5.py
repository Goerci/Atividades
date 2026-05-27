conta = 0
while True:  # loop infinito
    print('Cardápio')
    print('1. Açaí 300ml - R$ 12')
    print('2. Mousse - R$ 6,50')
    print('3. Salada de frutas - R$ 10')
    print('4. Fechar a conta')
    escolha = int(input('Qual você deseja?: (Utilize numeros) '))
    if escolha == 1:
        conta += 12
    elif escolha == 2:
        conta+= 6.50
    elif escolha == 3:
        conta+=10
    elif escolha == 4:
        break
    else:
        print("Numero invalido!")
        continue
print(conta)
