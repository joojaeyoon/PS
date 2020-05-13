N = int(input())

m = []
visited = [[False for __ in range(N)] for _ in range(N)]

for i in range(N):
    m.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

counter = [0 for _ in range(N*N)]


def dfs(x, y, count, idx):
    global counter

    visited[x][y] = True
    counter[idx] += 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < N \
                and m[x][y] == m[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny, count+1, idx)


idx = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and m[i][j] != 0:
            dfs(i, j, 0, idx)
            idx += 1

print(idx)
for n in sorted(counter[:idx]):
    print(n)
