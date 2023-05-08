# Programmers - 할인행사
def solution(want, number, discount):
    answer = 0
    i = 0
    while (len(discount)-i > 9):
        
        temp_num = number.copy()
        for j in range(i, i+10):
            if discount[j] in want:
                temp_num[want.index(discount[j])] -= 1
        if any(temp_num) == False:
            answer += 1
        i += 1
    return answer


solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],	["chicken", "apple", "apple",
         "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
