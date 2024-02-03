
target = int(input("Enter a number: "))

total = 0
eventotal = 0

for number in range(1, target+1):
    total = total + number

for evennumber in range(2, target+1, 2):
    eventotal = eventotal + evennumber

print("The sum of numbers from 1 to " + str(target) + " is " + str(total))
print("The sum of even numbers from 1 to " + str(target) + " is " + str(eventotal))

