import sys
from heapq import heappop, heappush

T = int(input())


def dijkstra(start: int, edge: list, dist: list):
    dist[start] = 0

    heap = []

    heappush(heap, (0, start))

    while heap:
        cost, cur = heappop(heap)

        for c, nxt in edge[cur]:
            new_cost = cost+c
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heappush(heap, (new_cost, nxt))


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    edge = [[] for _ in range(n+1)]
    dist = [[sys.maxsize for _ in range(n+1)] for __ in range(4)]
    dest = []
    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())

        edge[a].append((d, b))
        edge[b].append((d, a))

    for _ in range(t):
        dest.append(int(sys.stdin.readline()))

    dijkstra(s, edge, dist[0])
    dijkstra(g, edge, dist[1])
    dijkstra(h, edge, dist[2])

    answer = set()
    for d in dest:
        if dist[0][d] == dist[0][g]+dist[1][h]+dist[2][d]:
            answer.add(d)
        if dist[0][d] == dist[0][h]+dist[2][g]+dist[1][d]:
            answer.add(d)

    print(*sorted(list(answer)))
