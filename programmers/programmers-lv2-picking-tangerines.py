# Programmers - 귤 고르기

def solution(k, tangerine):
    dedupe = list(set(tangerine))
    dic = {}
    for i in range(len(dedupe)):
        dic[dedupe[i]] = 0

    for i in range(len(tangerine)):
        dic[tangerine[i]] += 1

    values = sorted(dic.values(), reverse=True)
    sum = 0

    for i in range(0, len(values)):
        sum += values[i]
        if sum >= k:
            return i+1


solution(2,[1, 1, 1, 1, 2, 2, 2, 3])
