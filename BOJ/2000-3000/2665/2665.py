import sys
from collections import deque

n = int(input())

answer = sys.maxsize
maze = []
visited = [[(sys.maxsize, sys.maxsize) for _ in range(n)] for __ in range(n)]
visited[0][0] = (0, 0)
for _ in range(n):
    maze.append(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()

q.append((0, 0, 0, 0))

while q:
    x, y, cnt, change = q.popleft()

    if x == n-1 and y == n-1:
        answer = min(change, answer)

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if maze[ny][nx] == "1":
                if change < visited[ny][nx][1]:
                    visited[ny][nx] = (cnt+1, change)
                    q.append((nx, ny, cnt+1, change))
            else:
                if change+1 < visited[ny][nx][1]:
                    visited[ny][nx] = (cnt+1, change+1)
                    q.append((nx, ny, cnt+1, change+1))

print(answer)
