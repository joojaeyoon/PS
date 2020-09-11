# Programmers LV 3 등굣길

def solution(m, n, puddles):
    MAP = [[0 for _ in range(m+1)] for __ in range(n+1)]
    visit = [[False for _ in range(m+1)] for __ in range(n+1)]

    for p in puddles:
        visit[p[1]][p[0]] = True

    MAP[1][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if visit[i][j]:
                continue
            MAP[i][j] = (MAP[i-1][j]+MAP[i][j-1]) % 1000000007

    return MAP[n][m]


print(solution(4, 3, [[2, 2]]))
