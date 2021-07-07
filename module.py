from math import sqrt

# only started using this file as a module from problem 23 onwards

def is_prime(n: int) -> bool:
    """
    Calculates whether the given number is prime (True) or not (False)
    """
    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> list:
    """
    Calculates the fibonacci sequence while its length is less than n
    """
    fibonacci = [1, 1, 2]
    while len(fibonacci) < n:
        next_num = fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2]
        fibonacci.append(next_num)
    return fibonacci

def sieve(n: int) -> list:
    """
    Uses the Sieve of Eratosthenes to calculate prime numbers up to n (non-inclusive)
    """
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            for i in range(p*p, n, p):
                sieve[i] = False
    primes = []
    for i in range(1, n):
        if sieve[i] == True:
            primes.append(i)
    return primes

def divisors(n: int) -> list:
    """
    Returns all the divisors of a given integer (non-inclusive)
    """
    divs = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            divs.extend([i, n / i])
    return list(set(map(int, divs)))