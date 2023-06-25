import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True

def find_closest_prime(n):
    if is_prime(n):
        return 0

    smaller = larger = n
    while True:
        smaller -= 1
        larger += 1
        if is_prime(smaller):
            return n - smaller
        if is_prime(larger):
            return larger - n

# Example usage
N = int(input())
min_diff = find_closest_prime(N)
print(min_diff)
