# random module
# list

import random

def get_a_random_string():
    list = ["aa","bb","cc"]
    string_val = random.choice(list)
    return string_val

print(get_a_random_string())