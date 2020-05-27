import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze = []
min_count = N*M

visited = [[0 for _ in range(M)] for __ in range(N)]

for i in range(N):
    maze.append(list(map(int, sys.stdin.readline()[:-1])))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append([0, 0, 1])
visited[0][0] = 1

while len(queue) != 0:

    x, y, count = queue.popleft()

    if x == M-1 and y == N-1:
        min_count = min(count, min_count)
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx < M and ny >= 0 and ny < N and maze[ny][nx] == 1 and visited[ny][nx] == 0:
            visited[ny][nx] += visited[y][x]+1
            queue.append([nx, ny, count+1])

print(min_count)
