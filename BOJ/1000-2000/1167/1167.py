import sys
from heapq import heappush, heappop

V = int(input())
edge = [[] for _ in range(V+1)]

for _ in range(V):
    data = list(map(int, sys.stdin.readline().split()))[:-1]

    v = data[0]

    for i in range(1, len(data), 2):
        edge[v].append((data[i+1], data[i]))


def dijkstra(edge, start):
    dist = [sys.maxsize for _ in range(V+1)]
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        cost, cur = heappop(heap)

        for c, nxt in edge[cur]:
            new_cost = cost+c

            if dist[nxt] > new_cost:
                dist[nxt] = new_cost
                heappush(heap, (new_cost, nxt))

    return dist


dist1 = dijkstra(edge, 1)
tmp = max(dist1[1:])
idx = dist1.index(tmp)
dist2 = dijkstra(edge, idx)
tmp = max(dist2[1:])
idx2 = dist2.index(tmp)

print(dist2[idx2])
