# Programmers - 2019 카카오 개발자 겨울 인턴십 (튜플)
def solution(s):
    s=s.replace(",{","")
    s=s[2:len(s)-2]
    s=s.split("}")
    for i in range(len(s)):
        s[i]=s[i].split(",")
        s[i]=[int(j) for j in s[i]]
    s.sort(key=len)
    result=[s[0]]
    for i in range(1,len(s)):
        result.append([x for x in s[i] if x not in s[i-1]])
    result=[result[i][0] for i in range(len(result))]
    test=0
    return result