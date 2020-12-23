n = int(input())
count = [1000000]
count = count * 1000001
count[0:11] = [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]


def co(a):
    if a == 1:
        return 0
    elif count[a] != 1000000:
        return count[a]
    else:
        if a % 6 == 0:
            count[a] = min(co(int(a - 1)), co(int(a / 2)), co(int(a / 3))) + 1
        elif a % 3 == 0:
            count[a] = min(co(a - 1), co(int(a / 3))) + 1
        elif a % 2 == 0:
            count[a] = min(co(a - 1), co(int(a / 2))) + 1
        else:
            count[a] = co(a - 1) + 1
        #count[a] = min(count[a], co(a-1), co(int(a/2)) if a % 2 == 0 else 9999999, co(int(a/3)) if a % 3 == 0 else 9999999) + 1
        return count[a]


print(co(n))
