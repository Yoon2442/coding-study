# Programmers - 구명보트
def solution(people, limit):
    people = sorted(people)
    answer = 0
    i = 0
    j = len(people)-1
    while (i < j):
        if people[i]+people[j] > limit:
            people.pop()
        elif people[i]+people[j] <= limit:
            people.pop()
            i += 1
        j = len(people)-1
        answer += 1
    if i == j:
        answer += 1
    return answer


solution([70,  80, 50], 100)
