emplo_num = int(input("What's your employee number? \n"))
num_hours = float(input("How much hours did you work? \n"))
value_hour = float(input("How much do you earn per hour worked? \n"))
salary = num_hours * value_hour

print(f"Employee nº {emplo_num}, \n Earning {value_hour} per hour, working for {num_hours} hours, your salary is: {salary}")