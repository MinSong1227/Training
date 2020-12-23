def solution(numbers, hand):
    row = [3, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    col = [1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i
        elif i == 0 or i == 2 or i == 5 or i == 8:
            if abs(row[i] - row[left]) + abs(col[i] - col[left]) > abs(row[i] - row[right]) + abs(col[i] - col[right]):
                answer += 'R'
                right = i
            elif abs(row[i] - row[left]) + abs(col[i] - col[left]) < abs(row[i] - row[right]) + abs(col[i] - col[right]):
                answer += 'L'
                left = i
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i
                else:
                    answer += 'L'
                    left = i
    return answer


number = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hands = "right"
print(solution(number, hands))