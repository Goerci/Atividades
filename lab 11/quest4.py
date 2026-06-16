import random
pontos1 = 0
pontos2 = 0
cont = 0
while pontos1 < 50 or pontos2 < 50:
    cont += 1
    print(f"========== RODADA {cont} ==========")
    print(f"========== Pontuação atual ==========")
    print(f"Player 1: {pontos1}")
    print(f"Player 2: {pontos2}")
    p1 = int(input("Player 1: Tente adivinhar a soma dos dados: "))
    p2 = int(input("Player 2: Tente adivinhar a soma dos dados: "))
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    result = dado1+dado2
    print("🎲 Rolando os dados...")
    time.sleep(1)
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(result)
    if abs(result - p1) < abs(result - p2:)
        print("Player 1 Chegou mais perto")
        pontos1 += 5
    elif abs(result - p1) == abs(result - p2:)
        print("Empate")
        pontos1 += 2
        pontos2 += 2
    else:
        print("Player 2 Chegou mais perto")
        pontos2 += 5
    