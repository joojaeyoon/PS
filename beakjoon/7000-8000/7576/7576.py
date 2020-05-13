import sys
from collections import deque

M, N = map(int, input().split())

tomato = []
visited = [[-1 for _ in range(M)] for __ in range(N)]

for i in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append([j, i])
            visited[i][j] = 0


while len(q) != 0:
    x, y = q.popleft()

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]

        if nx >= 0 and nx < M and ny >= 0 and ny < N and tomato[ny][nx] == 0 and visited[ny][nx] == -1:
            visited[ny][nx] = visited[y][x]+1
            q.append([nx, ny])

result = 0

for i in range(N):
    result = max(result, max(visited[i]))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0 and visited[i][j] == -1:
            result = -1
            break
    if result == -1:
        break

print(result)
