import math

def solution(n):
    answer = 0
    rt = int(math.sqrt(n))
    if rt * rt != n:
        answer = -1
    else:
        answer = (rt+1) ** 2
    return answer