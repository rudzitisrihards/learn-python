# while loop = statement that will execute it's block of code as long as its condition remains true

# while something_is_true:
#   do something repeatedly

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)