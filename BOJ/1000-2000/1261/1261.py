from collections import deque
import sys

M, N = map(int, input().split())

dist = [[100000000 for _ in range(M)] for __ in range(N)]

m = []

for i in range(N):
    m.append(list(map(int, sys.stdin.readline()[:-1])))

q = deque()

q.append([0, 0])

dist[0][0] = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while len(q) != 0:

    x, y = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx and nx < M and 0 <= ny and ny < N:
            if m[ny][nx]:
                if dist[ny][nx] > dist[y][x]+1:
                    dist[ny][nx] = min(dist[y][x]+1, dist[ny][nx])
                    q.append([nx, ny])
            else:
                if dist[ny][nx] > dist[y][x]:
                    dist[ny][nx] = min(dist[y][x], dist[ny][nx])
                    q.append([nx, ny])


print(dist[-1][-1])
