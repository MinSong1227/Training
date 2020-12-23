def solution(n):
    answer = 0
    a = [1]
    a = a * 1000001
    for i in range(2, n+1):
        if a[i] == 0:
            continue
        else:
            j = 2
            while j * i < n+1:
                a[i*j] = 0
                j += 1

    for i in range(2, n+1):
        if a[i] == 1:
            answer += 1
    return answer

print(solution(10))