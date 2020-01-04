def prime_number_series(num):
    for i in range(2, num + 1):
        if i == 2 or i == 3 or i == 5 or i == 7:
            print(i, end=' ')
        elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            prime = True
            for j in range(11, (i // 2) + 1, 2):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                print(i, end=' ')


prime_number_series(1000)
