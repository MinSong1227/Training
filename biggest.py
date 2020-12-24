def solution(numbers):
    answer = ''
    a = [str(i)*3 for i in numbers]
    a.sort(reverse=True)
    print(a)
    for i in a:
        answer += i[0:int(len(i)/3)]
    if answer[0] == '0':
        answer = '0'
    return answer


print(solution([0, 0, 0, 0, 0]))
