def prime_rectangle(height, width, start):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(num):
        next_num = num + 1
        while not is_prime(next_num):
            next_num += 1
        return next_num

    primes = []
    current_num = next_prime(start - 1)

    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(current_num)
            current_num = next_prime(current_num)
        primes.append(row)

    total_bilangan = sum(sum(row) for row in primes)
    for row in primes:
        print(" ".join(str(num) for num in row))
    print(total_bilangan)

prime_rectangle(2, 3, 13) # height = 2 width = 3
prime_rectangle(3, 2, 13) # height = 3 width = 2
prime_rectangle(5, 2, 1) # height = 5 width = 2
prime_rectangle(2, 5, 1) # height = 2 width = 5