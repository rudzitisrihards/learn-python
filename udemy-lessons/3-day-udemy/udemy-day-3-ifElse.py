
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
    else:
        bill = 12
        print("The ticket costs $" + str(bill))
    
    photo = input("Do you want your photo taken as well? Y or N")
    if photo == "Y":
        bill = bill + 3
    
    print("Your final bill is $" + str(bill))

else:
    print("You can NOT ride")