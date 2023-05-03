func_num = int(input("Qual o seu nº de funcionário? \n"))
num_horas = float(input("Quantas horas você trabalhou? \n"))
valor_hora = float(input("Quanto você ganha por hora trabalhada? \n"))
salario = num_horas * valor_hora

print(f"Funcionário nº {func_num}, \n Ganhando {valor_hora} por hora, trabalhando por {num_horas} horas, seu salário é de: {salario}")