import sys
from heapq import heappop, heappush

N, M = map(int, input().split())
dist = [sys.maxsize for _ in range(N+1)]
edge = [[]for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a].append((c, b))
    edge[b].append((c, a))

heap = []
dist[1] = 0

routes = [[]for _ in range(N+1)]

heappush(heap, (0, 1, [1]))

while heap:
    cost, cur, route = heappop(heap)

    for c, nxt in edge[cur]:
        new_cost = cost+c

        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            routes[nxt] = route+[nxt]
            heappush(heap, (new_cost, nxt, route+[nxt]))
answer = set()

for r in routes:
    if not r:
        continue
    for i in range(len(r)-1):
        answer.add((r[i], r[i+1]))

print(len(answer))
for a in answer:
    print(*a)
