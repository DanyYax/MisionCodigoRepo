#
# Example for Classes in Python
# Subscribe to Mision Codigo in YouTube
# https://www.youtube.com/c/misioncodigo?sub_confirmation=1
#

class Person:
    def __init__(self, name, weight):
        self.name = name
        self.age = 0
        self.weight = weight
    
    def say_hi(self):
        print(f"Hi, I'm {self.name}")

    def sleep(self):
        pass

    def birthday(self):
        self.age += 1
        self.say_hi()
        print(f"and I'm {self.age} years old")    

class Parent(Person):
    def __init__(self, name, weight, num_kids):
        super().__init__(name, weight)
        self.no_kids = num_kids

    def sleep(self):
        print(f"{self.name} you know that Parents don't sleep ...")

    def put_kids_to_bed(self):
        for k in range(self.no_kids):
            print(f"Kid {k + 1} is now in bed")

# main code
print("This is the main code")

# Use the class
me = Person("Chuck", 180)
print(f"{me.name} is {me.age} years old")
me.sleep()
me.birthday()

print()
friend = Person("Linus", 160)
friend.birthday()

me.birthday()

print(f"{me.name} is {me.age} years old")
print(f"{friend.name} is {friend.age} years old")

mom = Parent("Mom", 90, 3)
mom.birthday()
mom.sleep()
