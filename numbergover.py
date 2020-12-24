def solution(n):
    answer = ''
    a = []
    while n > 3:
        if n % 3 == 0 :
            a.append(3)
            n = int(n/3) -1
        else:
            a.append(n % 3)
            n = int(n/3)
    a.append(n)
    for i in a:
        if i == 1:
            answer = '1' + answer
        elif i == 2:
            answer = '2' + answer
        elif i == 3:
            answer = '4' + answer
    return answer


print(solution(11))
