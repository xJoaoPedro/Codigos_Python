preco_fabrica = float(input("Escreva o preço de fábrica do computador: \n"))
imposto = float(preco_fabrica * 0.3)
revenda = float(preco_fabrica * 0.1)
preco_final = preco_fabrica + imposto + revenda
print(f"O preço final do computador será de: {preco_final}")