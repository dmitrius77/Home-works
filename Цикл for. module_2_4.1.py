numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes = [] # создан пустой список
primes = []     # создан пустой список
for elem in numbers:
    if elem < 2: # если число меньше 2, то игнорирует дальнейшие строки
        continue    #  игнорировать число, если меньше 2
    is_prime = True
    for div in range(2, elem):
        if elem % div == 0:  # если число делится без остатка, то оно сложное
            not_primes.append(elem) # добавляем число к сложным
            is_prime = False  # во всех иных случаях число добавляется к простым
            break
    if is_prime:
        primes.append(elem)
print(primes)
print(not_primes)