import sys
from heapq import heappop, heappush


def dijkstra(start, end, edge, dist):
    answer = sys.maxsize
    answer_p = []
    dist[start] = 0

    heap = []

    heappush(heap, (0, start, [start]))

    while heap:
        cost, cur, path = heappop(heap)

        if cur == end and cost < answer:
            answer = cost
            answer_p = path

        for i in range(1, n+1):
            if edge[cur][i] != -1:
                new_cost = cost+edge[cur][i]
                if new_cost < dist[i]:
                    dist[i] = new_cost
                    heappush(heap, (new_cost, i, path+[i]))

    return answer_p


n = int(input())
m = int(input())

edge = [[-1 for __ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    if edge[a][b] != -1:
        edge[a][b] = min(edge[a][b], c)
    else:
        edge[a][b] = c

start, end = map(int, input().split())
dist = [sys.maxsize for _ in range(n+1)]

answer = dijkstra(start, end, edge, dist)

print(dist[end])
print(len(answer))
print(*answer)
