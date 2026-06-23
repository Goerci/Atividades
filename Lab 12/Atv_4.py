import random
import time

print("Prepare seu dedo no ENTER...")

# Gera um tempo de espera aleatório entre 2 e 10 segundos
tempo_espera = random.randint(2, 10)
time.sleep(tempo_espera)

# Alerta o usuário e começa a cronometrar
print("\nAGORA!")
tempo_inicial = time.time()

# Aguarda o clique do usuário
input()

# Registra o tempo final e calcula a diferença
tempo_final = time.time()
tempo_reacao = tempo_final - tempo_inicial

print(f"Você levou {tempo_reacao:.4f} segundos para pressionar ENTER!")