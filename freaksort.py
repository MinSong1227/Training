def solution(strings, n):
    answer = []
    answer.insert(0, strings[0])
    for i in strings[1:]:
        index = len(answer) - 1
        while index >= 0 and i[n] <= answer[index][n]:
            if i[n] == answer[index][n] and i > answer[index]:
                break
            index -= 1
        answer.insert(index+1, i)
    return answer

string = ["abce", "abcd", "cdx"]
#string = ["sun", "bed", "car"]
n = 2
print(solution(string, n))
