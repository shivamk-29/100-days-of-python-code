#making a tip calculator

#printing a welcome message
print("Welcome to the tip calculator!")

#taking user inputs for bill amount, tip percentage, and number of people
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#calculating the total amount after adding the tip
amount_after_tip = bill + (bill * (tip/100))

#calculating the amount each person should pay
amount_per_person = amount_after_tip / people

#printing the amount each person should pay, formatted to 2 decimal places
print(f"Each person should pay: ${amount_per_person:.2f}")