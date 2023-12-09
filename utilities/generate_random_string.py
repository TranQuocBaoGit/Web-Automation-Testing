import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters)) for i in range(int(length)))
    return result_str