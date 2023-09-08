A = float(input("Escreva o número A: "))
B = float(input("Escreva o número B: "))
C = float(input("Escreva o número C: "))

if (A > B and A > C):
    print(f"O maior número é o da letra A: {A}")
elif (B > A and B > C):
    print(f"O maior número é o da letra B: {B}")
elif (C > A and C > B):
    print(f"O maior número é o da letra C: {C}")