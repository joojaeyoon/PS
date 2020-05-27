import sys

N, M = map(int, input().split())

square = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

moves = [[[0, 0], [0, 1], [1, 1], [0, 2]],
         [[0, 0], [0, 1], [-1, 1], [1, 1]],
         [[0, 0], [0, 1], [-1, 1], [0, 2]],
         [[0, 0], [1, 0], [1, 1], [2, 0]]]

max_total = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def check(x, y):
    global max_total

    for move in moves:
        new_points = []
        total = 0
        for p in move:
            x = i+p[0]
            y = j+p[1]
            if x >= 0 and x < N and y < M and y >= 0:
                new_points.append([x, y])
                total += square[x][y]
        if len(new_points) == 4:
            max_total = max(max_total, total)


def dfs(depth, x, y, previous, sumVal):

    global max_total

    sumVal += square[x][y]

    if depth == 4:
        max_total = max(sumVal, max_total)
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M and [nx, ny] != previous:
            dfs(depth+1, nx, ny, [x, y], sumVal)


for i in range(N):
    for j in range(M):
        check(i, j)
        dfs(1, i, j, [], 0)

print(max_total)
