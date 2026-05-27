N = int(input("Quantos números quer digitar?"))
contador = 0
impares = 0
while contador <= N: #'while contador <= 0' para terminar o codigo
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1 #"Aqui deveria diminuir o contador e salvar o valor se é impar mas so adiciona valor ao impar "
        #contador +=1
print(f"Quantidade de ímpares entre 1 e {N}: {impares}") 
