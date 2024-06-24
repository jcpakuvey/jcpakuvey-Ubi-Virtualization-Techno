import timeit

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def benchmark():
    setup_code = """
from __main__ import generate_primes
"""
    stmt = "generate_primes(1000)"
    times = timeit.repeat(stmt, setup=setup_code, repeat=3, number=100)
    print(f"Tempo de execução: {min(times)}")

if __name__ == "__main__":
    generator = generate_primes(1000)
    print(generator)
    benchmark()