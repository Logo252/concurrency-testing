import time
import string
import random

SIZES = [12 for x in range(1_000_000)]


def generate_random_password(size):
    """
    Generate a password that has a minimum of one uppercase, one lowercase, one digit, and one special character
    """
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(size - 4):
        password += random.choice(all_chars)

    print(f"Generated password: {password}. Size: {size}")


if __name__ == "__main__":
    start_time = time.time()

    for number in SIZES:
        generate_random_password(number)

    duration_in_s = (time.time() - start_time)
    print(f"Finished in {duration_in_s} seconds")
