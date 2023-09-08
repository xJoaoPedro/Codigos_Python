num1 = input("Write a number: ")
num2 = input("Write other number: ")

remain1 = float(num1) % 2
remain2 = float(num2) % 2

if (remain1 == 0):
    print(f"{num1} is a multiple of 2.")
else:
    print(f"{num1} is not a multiple of 2.")

if (remain2 == 0):
    print(f"{num2} is a multiple of 2.")
else:
    print(f"{num2} is not a multiple of 2.")
