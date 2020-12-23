def solution(n):
    a = []
    while int(n) != 0:
        a.append(int(n) % 3)
        n /= 3
    answer = 0
    for i in range(len(a)):
        answer += a[i] * (3 ** (len(a)-i-1))
    return answer


print(solution(45))