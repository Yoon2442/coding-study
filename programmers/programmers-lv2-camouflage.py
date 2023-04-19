# Programmers - 위장
def solution(clothes):
    answer = 1
    clothes_dict=dict()
    for i in range(len(clothes)):
        if clothes[i][1] in clothes_dict:
            clothes_dict[clothes[i][1]].append(clothes[i][0])
        else:
            clothes_dict[clothes[i][1]]=[clothes[i][0]]
    
    for i in clothes_dict.keys():
        print(len(clothes_dict[i]))
        answer*=(1+len(clothes_dict[i]))
    return answer-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])