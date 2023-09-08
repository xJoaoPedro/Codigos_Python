num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

resto1 = float(num1) % 2
resto2 = float(num2) % 2

if (resto1 == 0):
    print(f"{num1} é múltiplo de 2")
else:
    print(f"{num1} não é múltiplo de 2")

if (resto2 == 0):
    print(f"{num2} é múltiplo de 2")
else:
    print(f"{num2} não é múltiplo de 2")