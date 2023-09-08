age = int(input("What is your age: "))

if (age >= 0 and age < 18):
    print("You're underage.")
elif (age <= -1):
    print("You're a liar!")
else:
    print("You're adult.")