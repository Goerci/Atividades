import random
import time

# Sorteia o número misterioso N entre 0 e 10
N = random.randint(0, 10)

print(f"O número misterioso sorteado foi: {N}\n")

# O laço range(1, N + 1) faz a contagem começar em 1 e terminar exatamente em N
for volta in range(1, N + 1):
    print(f"Volta {volta}: Mais uma volta!")
    time.sleep(1)  # Pausa de 1 segundos