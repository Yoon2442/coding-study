def solution(arr):
    answer = 1
    count = 0
    while count != len(arr):
        for i in range(0, len(arr)):
            if (answer % arr[i] == 0):
                count += 1
                pass
            else:
                count = 0
                answer += 1
                break
        
    print(answer)
    return answer


solution([2, 6, 8, 14])
