def solve(l, r):
    prime = []
    for i in range(l, r + 1):
        if identify_prime(i):
            prime.append(i)
    # Convert the list of primes to a space-separated string
    prime_str = " ".join(map(str, prime))
    print(prime_str)

def identify_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2

