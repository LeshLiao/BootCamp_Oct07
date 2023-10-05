# Random Module
import random

def get_a_target():
    return random.choice(['a cute dog','a cat','a bird'])

def get_a_place():
    place_list = ['on the beach','in a house','in the snow']
    return random.choice(place_list)

print(get_a_target() + " " + get_a_place())
