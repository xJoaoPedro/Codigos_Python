num1 = float(input("Write the first number: "))
num2 = float(input("Write the second number: "))

sum = num1 + num2
sub = num1 - num2

if (num1 > num2):
    print(f"The sum: {sum}")
elif (num2 > num1):
    print(f"The subtraction: {sub}")