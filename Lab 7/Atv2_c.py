maior = float('inf') #aqui o inf tem que ser negativo pois se não o maior nunca será alterado
#soma = 0
while soma <= 10: #não tem a variavel soma definida o codigo nem vai rodar, e não tem um contador 
    num = int(input("Digite um número: "))#soma += 1
    if num > maior:
       maior = num
print('O maior número é', maior)
