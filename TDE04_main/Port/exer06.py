num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
sub = num1 - num2

if (num1 > num2):
    print(f"A soma: {soma}")
elif (num2 > num1):
    print(f"A subtração: {sub}")