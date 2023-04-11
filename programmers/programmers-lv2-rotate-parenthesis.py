def solution(s):
    answer = 0
    stack = []
    string_length = len(s)
    for i in range(string_length):
        s = s+s[0]
        s = s[1:len(s)]
        for j in range(string_length):
            if s[j] == "(" or s[j] == "{" or s[j] == "[":
                stack.append(s[j])
            else:
                if s[j] == ")":
                    if len(stack) == 0:
                        stack.append(s[j])
                        continue
                    if stack[-1] == "(":
                        stack.pop()
                elif s[j] == "}":
                    if len(stack) == 0:
                        stack.append(s[j])
                        continue
                    if stack[-1] == "{":
                        stack.pop()
                elif s[j] == "]":
                    if len(stack) == 0:
                        stack.append(s[j])
                        continue
                    if stack[-1] == "[":
                        stack.pop()
                else:
                    stack.append(s[j])
        if len(stack) == 0:
            answer += 1
        else:
            stack.clear()
    return answer


solution("}}}")
