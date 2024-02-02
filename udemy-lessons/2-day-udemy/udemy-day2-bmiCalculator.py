
# >>> BMI CALCULATOR

print("This is a BMI calculator!")
weight = input("What is your weight in kg?\n")
print("Weight input is " + str(weight) + " kg")
height = input("How tall are you in cm?\n")
print("Height input is " + str(height) + " cm")

bmi = float(weight) / (float(height) **2)
bmi_rounded = round(bmi, 2)

print("Your body mass index is " + str(bmi_rounded))