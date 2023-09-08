A = float(input("Write the value of A: "))
B = float(input("Write the value of B: "))
C = float(input("Write the value of C: "))

if (A > B and A > C):
    print(f"The higher number is from letter A: {A}.")
elif (B > A and B > C):
    print(f"The higher number is from letter B: {B}.")
elif (C > A and C > B):
    print(f"The higher number is from letter C: {C}.")