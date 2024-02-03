
numbers = input("Input a list of numbers: ").split()

for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])

print(numbers)

highest_number = 0

for number in numbers:
    if number > highest_number:
        highest_number = number

print(highest_number)

