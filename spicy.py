

def solution(scoville, K):
    answer = 0
    while scoville[0] < k and len(scoville) > 1:
        sc = scoville[0] + scoville[1] * 2
        scoville[0:2] = []
        print(scoville)
        for i in range(len(scoville)):
            if sc <= scoville[i]:
                scoville.insert(i, sc)
                break
        answer += 1
        print(scoville)
    return answer


sco = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(sco, k))
