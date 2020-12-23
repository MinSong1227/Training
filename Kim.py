def solution(seoul):
    for i in seoul :
        if i == "Kim":
            index = seoul.index("Kim")
    answer = '김서방은 ' + str(index) +'에 있다'
    return answer


a = ["Jane", "Kim"]
print(solution(a))