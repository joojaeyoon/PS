import sys
from collections import deque

N, M = map(int, input().split())

m = []

for i in range(N):
    m.append(list(map(int, sys.stdin.readline()[:-1])))


def bfs():
    Q = deque()
    visited = [[[0, 0] for _ in range(M)] for __ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    Q.append([0, 0, False])
    visited[0][0][0] = 1

    while len(Q) != 0:

        x, y, crashed = Q.popleft()

        if x == M-1 and y == N-1:
            break

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx and nx < M and 0 <= ny and ny < N:
                if m[ny][nx] == 1 and not crashed:
                    visited[ny][nx][not crashed] = visited[y][x][crashed]+1
                    Q.append([nx, ny, not crashed])
                elif m[ny][nx] == 0 and not visited[ny][nx][crashed]:
                    visited[ny][nx][crashed] = visited[y][x][crashed]+1
                    Q.append([nx, ny, crashed])

    result = visited[N-1][M-1]

    if sum(result) == 0:
        print(-1)
    else:
        print(max(result))


bfs()
