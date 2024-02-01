# >>> BMI CALCULATOR

# print("This is a BMI calculator!")
# weight = input("What is your weight in kg?\n")
# print("Weight input is " + str(weight) + " kg")
# height = input("How tall are you in cm?\n")
# print("Height input is " + str(height) + " cm")
#
# bmi = float(weight) / (float(height) **2)
# bmi_rounded = round(bmi, 2)
#
# print("Your body mass index is " + str(bmi_rounded))


# >>> DEATH CALCULATOR

# print("Let's find out how many weeks you have left to live!")
#
# age = int(input("What is your age right now?\n"))
# death = int(input("What age will you be when you die?\n"))
# weeksLived = age * 52
# weeksLeft = (death - age) * 52
#
# print("You have lived for " + str(weeksLived) + " weeks, and you have " + str(weeksLeft) + " weeks left to live by the time you reach the age of " + str(death) + "!")


# >>> TIP CALCULATOR

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill in $?"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill"))

if people > 0:
    tip_amount = bill * (tip / 100)
    total_bill = bill + tip_amount
    pay_each = total_bill / people
    pay_each_formatted = "{:.2f}".format(pay_each) # this is for always displaying 2 numbers after decimal
    print("Each person should pay $" + pay_each_formatted)
else:
    print("Number of people must be greater than zero")