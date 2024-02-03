import time

# for loop = statement that will execute it's block of code for a limited amount of times

# for item in list_of_items:
#    do something to each item


fruits = ["Apple", "Peach", "Pear"]
for item in fruits:
    print(item)

for i in range(10):
    print(i)

for i in range(50, 60+1):
    print(i)

for i in "Rihards":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")