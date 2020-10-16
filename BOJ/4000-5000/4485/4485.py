import sys
from heapq import heappop, heappush

idx = 1
while True:
    N = int(input())

    if N == 0:
        break

    cave = []
    visited = [[sys.maxsize for _ in range(N)] for __ in range(N)]

    for _ in range(N):
        cave.append(list(map(int, sys.stdin.readline().split())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    heap = []
    heappush(heap, (cave[0][0], 0, 0))

    while heap:
        cost, x, y = heappop(heap)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] > cost+cave[ny][nx]:
                    visited[ny][nx] = cost+cave[ny][nx]
                    heappush(heap, (visited[ny][nx], nx, ny))

    print(f"Problem {idx}: {visited[N-1][N-1]}")
    idx += 1
