import sys

sys.setrecursionlimit(10**8)
M, N = map(int, input().split())
answer = 0

MAP = []

for _ in range(M):
    MAP.append(list(map(int, sys.stdin.readline().split())))

dp = [[-1 for _ in range(N)]for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):

    if x == N-1 and y == M-1:
        return 1
    if dp[y][x] >= 0:
        return dp[y][x]
    if dp[y][x] == -1:
        dp[y][x] = 0

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx and nx < N and 0 <= ny and ny < M and \
                MAP[ny][nx] < MAP[y][x]:
            dp[y][x] += dfs(nx, ny)

    return dp[y][x]


dfs(0, 0)

print(dp[0][0])
