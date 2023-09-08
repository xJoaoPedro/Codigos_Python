numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite o segundo número: "))

primeiro_maior = numero1 - numero2
segundo_maior = numero2 - numero1

if (numero1 > numero2):
    print(f"O primeiro é maior, portanto a diferença é de {primeiro_maior}")
elif (numero2 > numero1):
    print(f"O segundo é maior, portanto a diferença é de {segundo_maior}")
else:
    print("Os dois são iguais, então a diferença é de 0")