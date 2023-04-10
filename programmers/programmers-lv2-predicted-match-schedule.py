# Programmers - 예상 대진표
def solution(n, a, b):
    answer = 1
    while (a <= n and b <= n):
        if(abs(a-b) == 1 and a//2!=b//2):
            break
        print(a, b, answer)
        if a % 2 == 0:
            a = a//2
        elif a % 2 == 1:
            a = a//2+1
        if b % 2 == 0:
            b = b//2
        elif b % 2 == 1:
            b = b//2+1
        n = n/2
        answer += 1

    return answer


solution(8, 1, 2)
