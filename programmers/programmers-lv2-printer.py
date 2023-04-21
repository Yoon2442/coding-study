# Programmers - 프린터
def solution(priorities, location):
    answer = 0
    while len(priorities)>0:
        print(priorities,location,answer)
        if len([i for i in priorities if i>priorities[0]])==0:
            if location == 0:
                answer+=1
                return answer
            else:
                priorities.pop(0)
                location-=1
                answer+=1
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            location-=1
            if location<0 :
                location=len(priorities)-1
        

