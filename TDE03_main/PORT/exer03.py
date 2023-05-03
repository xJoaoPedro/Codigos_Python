preco_produto = float(input("Quanto está a unidade do produto? \n"))
quantidade = float(input("Quantas unidades você comprou? \n"))
pagamento = float(preco_produto * quantidade)
print(f"Você deve pagar R${pagamento} pela sua compra.")