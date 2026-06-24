import random
import time

print("Prepare o dedo no ENTER e aguarde o sinal...")

# Gera um tempo de espera aleatório entre 2 e 10 segundos e faz a pausa
tempo_espera = random.randint(2, 10)
time.sleep(tempo_espera)

# Exibe o sinal e guarda o tempo inicial exato
print("\nAGORA!")
tempo0 = time.time()

# Aguarda o usuário pressionar ENTER
input()

# Guarda o tempo final e calcula a diferença
tempo1 = time.time()
tempo_final = tempo1 - tempo0

print(f"Você levou {tempo_final:.4f} segundos para responder!")