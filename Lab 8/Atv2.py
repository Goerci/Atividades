cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
    print(f'{num} é um número ímpar')
#se o if der false imprime que o numero é impar e diminui o contador
#se o if der true não imprime nada e repete o codigo alem de diminuir o contador