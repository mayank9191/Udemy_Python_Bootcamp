class User:
  # Constructor
    def __init__(self, id, username):
        # print("new user being created...")
        # Attributes
        self.id = id
        self.username = username
        self.followers = 0  # Default attribute
        self.following = 0

    # Methods

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Mayank")
user_2 = User("002", "Rohan")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
