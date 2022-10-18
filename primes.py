"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from math import ceil


def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number of primes must be > 0.")

    prime_numbers = [2] # [1,2,3,4]
    n = 3

    while len(prime_numbers) < number_of_primes:
        for p in [p for p in prime_numbers if p <= ceil(n / 2)]:
            if not n % p:
                break 
        else:
            prime_numbers.append(n)
        n += 1

    return prime_numbers

if __name__ == "__main__":
    print(primes(200))