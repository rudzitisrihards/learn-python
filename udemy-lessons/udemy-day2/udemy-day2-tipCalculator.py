
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