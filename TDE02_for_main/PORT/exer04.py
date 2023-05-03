peso = float(input("Qual seu peso em kg? \n"))
altura = float(input("Qual a sua altura em m? \n"))
imc = peso / (altura ** 2)

print(f"\n Pesando {peso} e medindo {altura} seu IMC é de: {imc}")