def solution(answers):
    answer = [0, 0, 0]

    w1 = [1, 2, 3, 4, 5]
    w2 = [2, 1, 2, 3, 2, 4, 2, 5]
    w3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)) :
        if w1[i % 5] == answers[i] :
            answer[0] += 1
        if w2[i % 8] == answers[i] :
            answer[1] += 1
        if w3[i % 10] == answers[i] :
            answer[2] += 1

    ans = []
    if max(answer) == answer[0] :
        ans.append(1)
    if max(answer) == answer[1] :
        ans.append(2)
    if max(answer) == answer[2] :
        ans.append(3)
    return ans
