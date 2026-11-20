"""
Project 118: Prime Number Analyzer & Sieve Generator
Concepts: math algorithms, boolean filtering, Sieve of Eratosthenes, prime factorization.
"""
import math

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
    return [p for p in range(2, limit + 1) if primes[p]]

def main():
    print("=== PRIME NUMBER TOOLKIT ===")
    while True:
        print("\n1. Check if number is prime")
        print("2. Find prime factors of number")
        print("3. Generate all primes up to N (Sieve)")
        print("4. Exit")
        c = input("Choose (1-4): ").strip()
        if c == "1":
            n = int(input("Enter integer: "))
            print(f"-> {n} is {'PRIME' if is_prime(n) else 'NOT prime'}.")
        elif c == "2":
            n = int(input("Enter integer to factor: "))
            print(f"Prime factors: {' × '.join(map(str, prime_factors(n)))}")
        elif c == "3":
            limit = int(input("Upper limit (e.g., 100): "))
            plist = sieve(limit)
            print(f"Found {len(plist)} primes: {plist}")
        elif c == "4":
            break

if __name__ == "__main__":
    main()
