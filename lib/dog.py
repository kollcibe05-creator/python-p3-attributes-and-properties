# !/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Rufus", breed="Chihuahua"):   
        self.name = name    
        self.breed = breed  
    def get_name(self):
        return self._name         
    def set_name(self, name):
        if type(name) == str   and 1 <=len(name) <= 25:    
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")  
    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed 
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed        
        else:    
            print("Breed must be in list of approved breeds.")       
    breed = property(get_breed, set_breed)                   
    pass

# rufus = Dog("Coolio", "Corgi")
# print(rufus.breed)
# print(rufus.name)

# error = Dog("rubyisasmartdogandnsjkabkdbkadbhad", "")
# # print(error.name)
# print(error.breed)
# list_ex = ["brian", "kim", "collo"]
# name = "colld"
# print(name in list_ex)

# class Car :
#     def __init__(self, name, owner="Collins Kibet"):
#         self.name = name
#         self.owner = owner
#     def intro (self):
#         print(f"Hi I am a {name} and my owner is {owner}")    

# benz = Car("Mercedes Benz", "Guido Von")

# print(getattr(benz, "color", "It doesn't exist bro"))     #error message

# setattr(benz, "owner", "Tesla")
# print(hasattr(benz, "color"))
# delattr(benz, "owner")   //deletes the attribute
# print(getattr(benz, "owner", "It doesn't exist bro"))     #the atrrib must be stringified 


# class Human:
#     species = "Homo sapiens"
#     def __init__(self, age):
#         self.age = age
#     def get_age(self):
#         print("Retrieving age")
#         return self._age    
#     def set_age(self, age):
#         if type(age) in (int, float) and (0<= age <= 120):
#             print(f"Setting the age to { age }")  
#             self._age = age
#         else:
#             print("Stop the cap! No way🤣")
#     age = property(get_age, set_age)    

# guido = Human(age = 112)
# print(guido.age)
# shosh = Human(age=199)
# print(shosh.age)