import sys

sys.setrecursionlimit(10**8)

dx = [0, 0, -1, 1, -1, 1, -1, 1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]


def dfs(m, visited, y, x, w, h):
    visited[y][x] = True

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >= 0 and nx < w and ny >= 0 and ny < h and m[ny][nx] == 1 and not visited[ny][nx]:
            dfs(m, visited, ny, nx, w, h)


while True:

    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    m = []
    count = 0
    visited = [[False for _ in range(w)] for __ in range(h)]

    for _ in range(h):
        m.append(list(map(int, sys.stdin.readline().split())))

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and m[i][j] != 0:
                dfs(m, visited, i, j, w, h)
                count += 1

    print(count)
