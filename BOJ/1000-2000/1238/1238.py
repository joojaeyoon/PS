import sys
from heapq import heappop, heappush

N, M, X = map(int, input().split())

ways = [[] for _ in range(N+1)]
dists = [[sys.maxsize for __ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    ways[a].append((c, b))

for A in range(1, N+1):
    dists[A][A] = 0
    heap = []

    for cost, n in ways[A]:
        dists[A][n] = cost
        heappush(heap, (cost, n))

    while heap:
        cost, cur = heappop(heap)

        for c, nxt in ways[cur]:
            new_cost = dists[A][cur]+c

            if new_cost < dists[A][nxt]:
                dists[A][nxt] = min(dists[A][nxt], new_cost)
                heappush(heap, (new_cost, nxt))
answer = 0

for i in range(1, N+1):
    answer = max(answer, dists[i][X]+dists[X][i])
print(answer)
