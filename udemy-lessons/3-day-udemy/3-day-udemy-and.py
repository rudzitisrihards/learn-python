
# if x > 1 and x < 10
# if x > 1 or x < 10

print("Welcome to the roller coaster!")
height = int(input("How tall are you in cm?"))
bill = 0

if height >= 120:
    age = int(input("How old are you?"))
    if age <= 12:
        bill = 5
        print("The ticket costs $" + str(bill))
    elif age <= 18:
        bill = 7
        print("The ticket costs $" + str(bill))
    elif age >= 45 and age <= 55:
        print("Have a free ride because of your midlife crysis!")
    else:
        bill = 12
        print("The ticket costs $" + str(bill))
    
    photo = input("Do you want your photo taken as well? Y or N")
    if photo == "Y":
        bill = bill + 3
    
    print("Your final bill is $" + str(bill))

else:
    print("You can NOT ride")