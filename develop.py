def solution(progresses, speeds):
    answer = []
    index = 0
    while index < len(progresses):
        count = 0
        for i in range(index, len(progresses)):
            progresses[i] += speeds[i]
        for i in progresses[index:]:
            if i >= 100:
                index += 1
                count += 1
            else:
                break
        if count != 0:
            answer.append(count)
    return answer


pro = [95, 90, 99, 99, 80, 99]
sp = [1, 1, 1, 1, 1, 1]
print(solution(pro, sp))
