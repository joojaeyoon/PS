# Programmers LV 3 단속카메라

def solution(routes):
    answer = 1
    routes.sort()

    tmp = routes[0][1]
    routes.pop(0)

    for r in routes:
        if r[0] <= tmp:
            tmp = min(tmp, r[1])
        else:
            tmp = r[1]
            answer += 1

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
