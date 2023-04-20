# Programmers - 기능개발
def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    count = 0

    while (len(progresses) > 0):
        progresses = [x+y for x, y in zip(progresses, speeds)]

        while len(progresses) > 0 and progresses[len(progresses)-1] >= 100:
            if progresses[len(progresses)-1] >= 100:
                progresses.pop()
                speeds.pop()
                count += 1
        
        answer.append(count)
        count = 0

    answer = [i for i in answer if i != 0]
    return answer


solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])
