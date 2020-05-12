import sys

sys.setrecursionlimit(10**8)

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]
rel = [[] for _ in range(N+1)]

count = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    rel[a].append(b)
    rel[b].append(a)


def dfs(num):
    visited[num] = True

    for r in rel[num]:
        if not visited[r]:
            dfs(r)


for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)
