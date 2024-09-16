numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
count = 0

primes = []
not_primes = []

for i in range(2, len(numbers) + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        primes.append(i)
    else:
        not_primes.append(i)
    count = 0

print('Primes: ',primes)
print('Not_primes: ', not_primes)

