def solution(dartResult):
    before = 0
    score = 0
    sum = 0
    ten = 0
    star = 0
    for i in range(len(dartResult)):
        if ten == 1:
            ten = 0
            sum += score
            if star == 0:
                before = score
            else:
                before = score - before
                star = 0
            score = 10
        elif 48 <= ord(dartResult[i]) <= 57:
            if ord(dartResult[i]) == 49 and ord(dartResult[i+1]) == 48:
                ten = 1
                continue
            sum += score
            if star == 0:
                before = score
            else:
                before = score - before
                star = 0
            score = ord(dartResult[i]) - 48
        elif dartResult[i] == 'S':
            score = score ** 1
        elif dartResult[i] == 'D':
            score = score ** 2
        elif dartResult[i] == 'T':
            score = score ** 3
        elif dartResult[i] == '#':
            score *= -1
        elif dartResult[i] == '*':
            star = 1
            score = score + before + score
    sum += score
    return sum


print(solution("1D2S#10S"))