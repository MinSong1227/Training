def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        aa = []
        bb = []
        for j in range(n):
            aa.append((arr1[i] % 2) + (arr2[i] % 2))
            #bb.append(arr2[i] % 2)
            arr1[i] = int(arr1[i]/2)
            arr2[i] = int(arr2[i]/2)
        aa.reverse()
        #bb.reverse()
        arr1[i] = aa
        #arr2[i] = bb
    for i in range(n):
        string = ''
        for j in range(n):
            if arr1[i][j] >= 1:
                string += '#'
            else:
                string += ' '
        answer.append(string)
    return answer


a = [9, 20, 28, 18, 11]
b = [30, 1, 21, 17, 28]
n = 5
print(solution(n, a, b))