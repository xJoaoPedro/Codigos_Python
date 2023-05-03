fact_price = float(input("Escreva o preço de fábrica do computador: \n"))
tax = float(fact_price * 0.3)
resale = float(fact_price * 0.1)
final_price = fact_price + tax + resale
print(f"The final price of the computer is: {final_price}")