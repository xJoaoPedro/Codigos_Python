idade = int(input("Qual a sua idade: "))

if (idade >= 0 and idade < 18):
    print("Você é menor de idade.")
elif (idade <= -1):
    print("É mentira!")
else:
    print("Você é maior de idade.")