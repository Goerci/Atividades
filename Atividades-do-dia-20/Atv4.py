import random # essa deve ser a primeira linha do código
chances = 5
numero = random.randint(1,10)
while chances > 0:
    palpite = int(input("Escolha um numero de 1 a 10: "))
    chances -= 1
    if numero == palpite:
        print("Parabens!, voce acertou")
        break
    elif numero > palpite:
        print("O numero é maior")
if chances == 0:
    print(f"Que pena... o numero era: {numero}")




















#O código a seguir gera aleatoriamente um número entre 1 e 10. Complete o código com uma lógica 
#parecida com a da questão anterior, dando 5 chances para o usuário acertar o número. Caso acerte, dê parabéns ao usuário.