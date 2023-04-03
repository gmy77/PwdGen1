
import string
import random


# Define the minimum and maximum password lengths
MIN_PASS_LENGTH = 8
MAX_PASS_LENGTH = 10

# Define the characters to be used in generating passwords
CHARACTERS = string.ascii_letters + string.digits + string.punctuation

# Generate 10 passwords
for _ in range(10):
    # Generate a random length for the password
    length = random.randint(MIN_PASS_LENGTH, MAX_PASS_LENGTH)
    # Generate the password with the selected length
    password = ''.join(random.choices(CHARACTERS, k=length))
    print(password)
