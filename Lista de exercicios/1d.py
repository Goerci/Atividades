import random

numero = random.randint(1, 10)

for i in range(3):
    n = int(input("Adivinhe o número: "))

    if n == numero:
        print("Correto")
        break

#Faltou import random.
#input() retorna texto. É necessário usar int() para comparar com o número sorteado.