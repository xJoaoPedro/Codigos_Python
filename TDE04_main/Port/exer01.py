A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A > B:
    print(f"Somando 100 ao valor de A ficamos com {A + 100}")
elif B > A:
    print(f"Somando 100 ao valor de B ficamos com {B + 100}")
else:
    print(f"Os dois são iguais, portanto: {A + 100}")