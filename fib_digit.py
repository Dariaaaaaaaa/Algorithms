# последняя цифра числа Фибоначчи

def fib_digit(n):
    a = []
    a.append(0)
    a.append(1)
    if n == 1:
        return 1
    else:
        for i in range(2, n+1):
            a.append((a[0] + a[1]) % 10)
            a = a[1:]
    return a[1]
