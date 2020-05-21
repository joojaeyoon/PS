def checkValidString(p):
    stack = []

    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        else:
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False

    if len(stack) != 0:
        return False

    return True


def solution(p):

    if checkValidString(p):
        return p

    idx = 0
    check = [0, 0]

    for i in range(len(p)):
        if p[i] == "(":
            check[0] += 1
        else:
            check[1] += 1

        if check[0] != 0 and check[0] == check[1]:
            idx = i
            break
    u, v = p[:idx+1], p[idx+1:]

    if checkValidString(u):
        return u+solution(v)

    tmp = "("
    tmp += solution(v)+")"

    for i in range(1, len(u)-1):
        if u[i] == "(":
            tmp += ")"
        else:
            tmp += "("

    return tmp


print(solution("()))((()"))
