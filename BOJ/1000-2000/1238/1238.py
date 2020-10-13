import sys
from heapq import heappop, heappush

N, M, X = map(int, input().split())

ways = [[] for _ in range(N+1)]
ways_back = [[] for _ in range(N+1)]
dist1 = [sys.maxsize for _ in range(N+1)]
dist2 = [sys.maxsize for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    ways[a].append((c, b))
    ways_back[b].append((c, a))


def dijkstra(ways, A, dist):
    dist[A] = 0
    heap = []

    for cost, n in ways[A]:
        dist[n] = cost
        heappush(heap, (cost, n))

    while heap:
        cost, cur = heappop(heap)

        for c, nxt in ways[cur]:
            new_cost = dist[cur]+c

            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heappush(heap, (new_cost, nxt))


dijkstra(ways, X, dist1)
dijkstra(ways_back, X, dist2)

answer = 0
for i in range(1, N+1):
    answer = max(answer, dist1[i]+dist2[i])
print(answer)
