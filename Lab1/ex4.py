import math


def is_prime(n):
    # Returns True if a number given is prime and False otherwise
    if(n < 2 or n % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(n)) + 2, 2):
        if n % i == 0:
            return False
    return True
