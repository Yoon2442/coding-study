def solution(n):
    answer = 0
    array=[1]
    for i in range(0,n):
        if(i==0):
            array.append(1)
        else:
            array.append(array[i]+array[i-1])
    answer=array[len(array)-1]%1234567

    return answer

solution(3)