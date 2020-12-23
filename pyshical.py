def solution(n, lost, reserve):
    answer = 0
    a = [0]
    a = a * 41
    for i in lost:
        a[i] -= 1
    for i in reserve:
        a[i] += 1
    for i in range(1, n+1):
        if a[i] == 1 and a[i-1] == -1:
            a[i] = 0
            a[i-1] = 0
        if i < n+1 and a[i] == 1 and a[i+1] == -1:
            a[i] = 0
            a[i+1] = 0
    for i in range(1, n+1):
        if a[i] >= 0:
            answer += 1
    return answer


n = 5
loss = [1, 2, 4, 5]
reserve = [2, 3, 4]
print(solution(n, loss, reserve))