import time

entrada = int(input("Quanto tempo de pausa?"))

tempo0 = time.time()
time.sleep(entrada * 2)
tempo1 = time.time()

print("Você esperou", int(tempo1-tempo0), "segundos")

#Entrada: 2  Saída: Você esperou 4 segundos
#Entrada: 100  Saída: Você esperou 200 segundos