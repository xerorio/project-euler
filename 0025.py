# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

from module import fibonacci

fibonacci_seq = fibonacci(5000)

# check that last number has at least 1000 digits
longest_num = fibonacci_seq[len(fibonacci_seq)-1]

for num in fibonacci_seq:
    if (len(str(num)) >= 1000):
        print(fibonacci_seq.index(num) + 1)
        break

# Answer: 4782