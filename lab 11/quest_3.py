import random
import time 
while True:
    quer = input("Quer fazer uma pergunta? s/n:  ")
    if quer == "n":
        break
    else:
        perg = input("Insira uma pergunta de sim ou não: ")
        prob = random.randint(1, 10)
        print("To pensando")
        time.sleep(2)
        print("Averiguando resenha")
        time.sleep(2)
        print("Entrega da shopee")
        time.sleep(2)
        if prob <=5:
            print("Sim!!!")
            continue
        else:
            print("Não")
            continue
            
    