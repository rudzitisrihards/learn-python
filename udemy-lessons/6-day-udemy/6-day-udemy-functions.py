# function = block of code that will execute only when it is called

# define function and define the parameters it can receive inside ()

def hello(firstname, lastname):
    print("Hello, " + firstname + " " + lastname + "!")
    print("Have a nice day!")

# obtain the parameters

userinput1 = input("What is your first name?")
userinput2 = input("What is your last name?")

# call function and provide the parameters

hello(userinput1, userinput2)