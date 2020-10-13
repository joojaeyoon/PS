import sys
from collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, sys.stdin.readline().split()))
    edge = [[] for _ in range(N+1)]
    pre_build_cnt = [0 for _ in range(N+1)]
    results = [0 for _ in range(N+1)]

    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())

        edge[a].append(b)
        pre_build_cnt[b] += 1

    W = int(input())

    q = deque()

    for i in range(1, N+1):
        if pre_build_cnt[i] == 0:
            results[i] = times[i]
            q.append((i, 0))

    for i in range(N):
        x, cnt = q.popleft()
        if x == W:
            break

        for j in range(len(edge[x])):
            n = edge[x][j]
            pre_build_cnt[n] -= 1
            results[n] = max(results[n], results[x]+times[n])
            if pre_build_cnt[n] == 0:
                q.append((n, cnt+1))
    print(results[W])
