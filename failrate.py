def solution(N, stages):
    answer = []
    fail = []
    for i in range(1, N+1):
        reach = 0
        success = 0
        for j in stages:
            if j > i:
                reach += 1
                success += 1
            elif j == i:
                reach += 1
        if reach == 0:
            fail.append([i,0])
        else:
            fail.append([i, 1 - success/reach])
    fail.sort(key=lambda rate: rate[1], reverse=True)
    for i in fail:
        answer.append(i[0])
    return answer

n = 5
stage = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stage))