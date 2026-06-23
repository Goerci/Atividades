# Leitura dos dados de entrada
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Cálculo da diferença absoluta
diferenca_absoluta = abs(num1 - num2)

# Arredondamento para 2 casas decimais
resultado_final = round(diferenca_absoluta, 2)

# Exibição do resultado
print(f"A diferença absoluta entre os números é: {resultado_final}")