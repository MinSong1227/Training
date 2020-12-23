
zero = 0
one = 0


def fibonacci(n):
    if n == 0:
        global zero
        zero = zero + 1
        return 0
    elif n == 1:
        global one
        one = one + 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


a = input()
for i in range(int(a)):
    zero = 0
    one = 0
    b = input()
    fibonacci(int(b))
    print(zero, one, "\n")
