
# >>> DEATH CALCULATOR

print("Let's find out how many weeks you have left to live!")

age = int(input("What is your age right now?\n"))
death = int(input("What age will you be when you die?\n"))
weeksLived = age * 52
weeksLeft = (death - age) * 52

print("You have lived for " + str(weeksLived) + " weeks, and you have " + str(weeksLeft) + " weeks left to live by the time you reach the age of " + str(death) + "!")