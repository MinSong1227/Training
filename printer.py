import queue


def solution(priorities, location):
    answer = 0
    q = queue.Queue()
    for i in priorities:
        q.put(i)
    while True:
        a = q.get()
    for i in range(location+1):
        answer = q.get()[1]
    return answer


print(solution([2, 1, 3, 2], 2))