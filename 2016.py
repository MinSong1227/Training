def solution(a, b):
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(0,a-1):
        day += mon[i]
    day += b
    answer = week[(day+4) % 7]
    return answer


print(solution(5, 24))