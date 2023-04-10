# Programmers - 카펫
def solution(brown, yellow):
    total = brown+yellow
    divisor = list([])
    for i in range(1, total+1):
        if (total % i == 0):
            divisor.append(i)

    for i in range(0, len(divisor)):
        if ((divisor[i]-2)*(divisor[len(divisor)-i-1]-2) == yellow):
            answer = [divisor[i], divisor[len(divisor)-i-1]]
    return answer
