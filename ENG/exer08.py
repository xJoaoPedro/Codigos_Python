time_spent = float(input("How long was the trip in hours? \n"))
average_speed = float(input("What was the average speed of the trip? \n"))
distance = time_spent * average_speed
fuel_spent = distance / 12
print(f"The amount of fuel spent on the trip was: {fuel_spent}")