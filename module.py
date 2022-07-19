from math import sqrt

def split_word(word: str) -> list:
    return [c for c in word]

def is_prime(n: int) -> bool:
    """
    Calculates whether the given number is prime (True) or not (False)
    """
    if n == 0 or n == 1:
        return False

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

def sieve(m: int, n: int) -> list:
    """
    Uses the Sieve of Eratosthenes to calculate prime numbers from m up to n (non-inclusive)
    """
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            for i in range(p*p, n, p):
                sieve[i] = False
    primes = []
    for i in range(m, n):
        if sieve[i]:
            primes.append(i)
    
    if 1 in primes:
        primes.remove(1)
    
    return primes

def divisors_i(n: int) -> list:
    """
    Returns all the divisors of a given integer (inclusive)
    """
    divs = [1, n]
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0) and i not in divs and (n / i) not in divs:
            divs.extend([i, n / i])
    return divs

def divisors_n(n: int) -> list:
    """
    Returns all the divisors of a given integer (non-inclusive)
    """
    divs = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0) and i not in divs and (n / i) not in divs:
            divs.extend([i, n / i])
    return divs

def is_palindromic(input_num: int) -> bool:
    """
    Determine whether the input number is palindromix
    """
    if (reverse_digits(input_num) == input_num):
        return True
    else:
        return False

def reverse_digits(num: int) -> int:
    """
    Reverse the digits of the input number
    """
    rev_num = 0
    while (num > 0):
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num

def bin_is_palindrome(num: int) -> bool:
    """
    Check if the binary equivalent base 10 integer is palindromic
    """
    binary = bin(num)
    binary = binary[2:]

    return binary == binary[-1::-1]

def gcd(a: int, b: int) -> int:
    """
    Returns greatest common divisor of two input numbers
    """
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def factorial(n: int) -> int:
    """
    Applies factorial function to input number
    """
    if isinstance(n, int) is False:
        print('Error: number is not an integer')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
