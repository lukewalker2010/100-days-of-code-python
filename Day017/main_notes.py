# Class is a Blueprint for creating an eventual object
# PascalCase for Classes
# camelCase -> first word lower case
# snake_case -> everything but classes

# Consturctor using the initalize function

class User:

    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Luke")
user_2 = User("002", "Angela")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)