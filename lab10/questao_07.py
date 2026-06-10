v = e = d = 0
for _ in range(int(input("Quantidade de jogos: "))):
    gols_galo = int(input())
    gols_op = int(input())
    
    if gols_galo > gols_op: v += 1
    elif gols_galo == gols_op: e += 1
    else: d += 1

print(f"Vitórias: {v}\nEmpates: {e}\nDerrotas: {d}\nPontuação: {v * 3 + e}") 