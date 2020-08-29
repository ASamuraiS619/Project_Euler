def primes_up_to(number):
    primes = set([i for i in range(3, number, 2)])
    tmp = set()
    while True:
        prime = min(primes)
        tmp.add(prime)
        if prime > number ** 0.5:
            primes = primes | tmp
            primes.add(2)
            return sorted(list(primes))
        else:
            primes = primes - set([i for i in range(prime, number, prime)])

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for divisor in range(3, int(num ** 0.5 + 1), 2):
            if num % divisor == 0:
                return False
        return True
