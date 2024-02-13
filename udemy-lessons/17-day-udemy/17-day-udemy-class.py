# class = blueprint for object
# object = constructed from class, has some attributes (variables) and methods (functions)

# attribute = variable associated with an object, something an object has
# method = function inside object, something an object does



class MyClass: # create class with a name
    def __init__(self): # define & initialize attributes
        print("initializing attributes")

    def action(self): # define method
        print("doing something") 

object_1 = MyClass() # create object which now has attributes and methods



class User:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Rihards")
user_2 = User("002", "Agnese")

user_1.follow(user_2)

print(f"{user_1.username} has {user_1.followers} followers")
print(f"{user_1.username} is following {user_1.following} users")
print(f"{user_2.username} has {user_2.followers} followers")
print(f"{user_2.username} is following {user_2.following} users")