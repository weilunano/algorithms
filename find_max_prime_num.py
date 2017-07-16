NUM = 600851475143


def find_max_prime_num():
    n = NUM
    factor = 2
    max_prime = 1

    while n > 1:
        if n % factor == 0:
            max_prime = factor
            n = n / factor
            while n % factor == 0:
                n = n / factor
        factor = factor + 1
    print max_prime

if __name__ == "__main__":
    find_max_prime_num()
