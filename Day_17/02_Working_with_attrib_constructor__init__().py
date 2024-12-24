class User:
    def __init__(self, id, username):
        # print("new user being created...")
        self.id = id
        self.username = username
        self.followers = 0  # Default attribute


user_1 = User("001", "Mayank")
# user_1.id = "001"
# user_1.username = "Mayank"


print(user_1.username)

# if we make a constructor and give some attributes you have to give all required value every time while  initializing a class

user_2 = User("002", "Rohan")
# user_1.id = "002"
# user_1.username = "Rohan"
