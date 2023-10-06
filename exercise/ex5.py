# Random Module Python Built-In Module

'''
Create a function call

get_a_animal()

    and create a animal_list in the function, ex: ['a dog','a cat']

when I call get_a_animal(), I can get a random animal.


Create another function call

get_a_place()

    and create a place_list in this function, ex: ['in the house','on the bus']

when I call get_a_place(), I can get a random place.



and then print it together.

ex:
a cat in the house

'''

import random

def get_a_animal():
    animal_list = ['a cute dog','a cat','a bird']
    return random.choice(animal_list)

def get_a_place():
    place_list = ['on the beach','in the house','in the snow']
    return random.choice(place_list)

if __name__ == '__main__':
    print(get_a_animal() + " " + get_a_place())