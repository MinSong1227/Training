def solution(board, moves):
    answer = 0
    stack = []
    for i in moves :
        j = 0
        while True :
            if(j >= len(board)):
                break
            elif board[j][i-1] == 0 :
                j = j + 1
            elif board[j][i-1] != 0 :
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
    pointer = 0
    for i in range(1, len(stack)):
        if(len(stack) >= 2):
            if(stack[pointer] == stack[pointer+1] and pointer <= len(stack) - 1):
                    stack[pointer:pointer+2] = []
                    answer = answer + 2
                    pointer = pointer - 2
            pointer = pointer + 1
    return answer


arr = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
move = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(arr, move))