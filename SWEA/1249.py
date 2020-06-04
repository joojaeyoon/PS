from collections import deque

T = int(input())

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

for t in range(T):

    N = int(input())

    m = [list(map(int, input())) for _ in range(N)]
    visited = [[987654321 for _ in range(N)] for __ in range(N)]

    q = deque()

    min_cost = 987654321

    q.append([0, 0, 0])

    while len(q) != 0:

        x, y, cost = q.popleft()

        if visited[x][y] <= cost:
            continue

        visited[x][y] = cost

        if x == N-1 and y == N-1:
            min_cost = min(min_cost, cost)
            continue

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if cost+m[nx][ny] < visited[nx][ny]:
                    q.append([nx, ny, cost+m[nx][ny]])

    print(f"#{t+1} {min_cost}")
