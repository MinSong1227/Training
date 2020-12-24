def solution(prices):
    a = [0] * len(prices)
    for i in range(len(prices)):
        if i == len(prices) - 1:
            break
        for j in prices[i+1:]:
            a[i] += 1
            if j < prices[i]:
                break
    return a


print(solution([1, 2, 3, 2, 3]))
