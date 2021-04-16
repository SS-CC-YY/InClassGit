import random
import string

a = string.ascii_letters+string.digits

key = []

def num_words():
    try:
        num_words = int (input("Please enter the length of the password: "))
        return num_words
    except:
        print("Invalid input!")

def generator_passwords():
    key = random.sample(a,num_words())
    keys = "".join(key)
    return keys

        
print(generator_passwords())

