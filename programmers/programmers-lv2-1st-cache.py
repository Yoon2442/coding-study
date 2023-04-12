# Programmers - [1차] 캐시
def solution(cacheSize, cities):
    answer = 0
    cache=[]
    
    for i in range(len(cities)):
        cities[i]=cities[i].lower()

        if cities[i] in cache:
            answer+=1
            cache.remove(cities[i])
            cache.append(cities[i])
        else:
            answer+=5
            cache.append(cities[i])
            if len(cache)>cacheSize:
                cache.pop(0)
    return answer

solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])