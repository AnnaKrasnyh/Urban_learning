numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False
for i in numbers[1::]:
    is_prime = True
    for j in range(2, i):
        if i % j == 0 and i != j:
            is_prime = False
            break
    if not is_prime :
        not_primes.append(i)
    else:
        primes.append(i)
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')