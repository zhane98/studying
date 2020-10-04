# class Person:
#     def __init__(self, name):
#         self.name = name 

# person = Person("Dave Smith")
# print(person.name)

# PARENT / blueprint
class Animal: #0 initiate an object/class to be reused
    def __init__(self, colour, first_name, last_name, age_int): #2 arguments get passed in the same order
        self.colour = colour #3 we assign arguments to parts of the object/class body
        self.first = first_name
        self.last = last_name
        self.age = age_int              #These are the different compartments in the empty box

    def rollover(self): # Adding a function/action called rollover to the blueprint for the clones to inherit.
        print(self.first + " rolls over")


# CHILD / clone
new_animal1 = Animal("Pink", "Tia", "Woods", 20) #1 pass in correct number of arguments.     We start adding things in order into the box/giving meaning.

# CHILD / clone
new_animal2 = Animal("Black", "Casius", "Clay", 120)

# print(new_animal1.first)
# print(new_animal2.first)

new_animal1.rollover() # The clones have now inherited the ability to rollover from their PARENT blueprint
new_animal2.rollover()

# This is how Inheritance works
# Chimp is a new Parent class based off of the Animal Parent Class.
# All initiations have to be copied but the functions are implicitly inherited 
class Chimp(Animal):
    def __init__(self, colour, first_name, last_name, age_int, breed):
        super().__init__(colour, first_name, last_name, age_int)
        self.colour = colour 
        self.first = first_name
        self.last = last_name
        self.age = age_int 
        self.breed = breed

    def smash_rocks(self):      #defining a new function
        print(self.first + ", go and smash the " + colour_of_rocks_to_smash + " rocks")

# CHILD of Chimp PARENT class.
leader = Chimp("Black", "Caesar", "Emperor", 40, "Silverback")

print(leader.first)
print(leader.breed)

leader.rollover()
leader.smash_rocks()
