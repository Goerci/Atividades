soma = 0

for i in range(10):

    if i == 3:
        continue

    if i == 7:
        break

    soma += i
    print(i, soma)

Valores de i:

0
1
2
4
5
6

Valores de soma:

0
1
3
7
12
18