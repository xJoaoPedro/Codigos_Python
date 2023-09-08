num1 = float(input("Write the first number: "))
num2 = float(input("Write the second number: "))

first_higher = num1 - num2
second_higher = num2 - num1

if (num1 > num2):
    print(f"The first number is higher, so the difference is {first_higher}.")
elif (num2 > num1):
    print(f"The second number is higher, so the difference is {second_higher}.")
else:
    print("Both numbers are equal, so the difference is 0.")