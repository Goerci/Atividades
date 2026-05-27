capacidade = 0
mochila = ''
while capacidade <= 5:
    item = input("Escolha o item que deseja guardar: ")
    mochila += item
    mochila += ','
    capacidade += 1
    sair = input("Deseja sair da mochila: ").lower()
    if sair == 'sim':
        print(f"items na mochila: {mochila}")
        break
if capacidade == 5:
    print(f"items na mochila: {mochila}")




























#Um herói de jogo pode carregar no máximo 5 itens. Escreva um código que peça ao usuário para adicionar itens à mochila (um por vez) escrevendo o nome de cada item.
#  Enquanto o número de itens for menor que 5, continue perguntando. Se o usuário digitar "sair", interrompa com break antes de encher a mochila. Ao final, mostre os itens na mochila.