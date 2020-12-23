ar = [0]
ar = ar * 41


def fibonacci(n, ar):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif ar[n] != 0:
        return ar[n]
    else:
        ar[n] = fibonacci(n-1, ar) + fibonacci(n-2, ar)
        return ar[n]


a = input()
# b = []
for i in range(int(a)):
    b = int(input())
    if b == 0:
        print(1, 0)
    else:
        print(fibonacci(b-1, ar), fibonacci(b, ar))
