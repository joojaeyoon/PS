# Programmers LV 3 네트워크

def find(n, computers, visited):

    visited[n] = True

    for i in range(len(computers)):
        if i != n and computers[n][i] == 1 and not visited[i]:
            find(i, computers, visited)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            answer += 1
            find(i, computers, visited)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # 2

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # 1
