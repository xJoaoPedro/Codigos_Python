numero_x = float(input("primeiro número: \n"))
numero_y = float(input("segundo número: \n"))
numero_z = float(input("terceiro número: \n"))
multipli = numero_x * numero_y * numero_z
soma = numero_x + numero_y + numero_z
subtração = numero_x - numero_y - numero_z
soma_total = soma + multipli + subtração
print(f"multiplicação: {multipli}")
print(f"soma: {soma}")
print(f"subtração: {subtração}")
print(f"a soma das operações: {soma_total}")