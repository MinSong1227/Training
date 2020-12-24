def solution(w, h):
    answer = 0
    if w>h:
        a = w
        b = h
    else:
        a = h
        b = w
    while b!=0:
        n = a % b
        a = b
        b = n
    answer = w*h -(w+h-a)
    return answer


print(solution(8, 12))
