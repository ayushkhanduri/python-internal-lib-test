import pickle

class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def increment_age(self):
        self.age += 1

user = User("Ayush", 28)
user.increment_age()
user.increment_age()
user.increment_age()

# used for storing data with their data types
with open('./serialise-obj.txt', "wb") as file:
    pickle.dump(user, file)

with open('./serialise-obj.txt', "rb") as file:
    u1: User = pickle.load(file)

u1.increment_age()
print(id(u1))
print(id(user)) #different ids
