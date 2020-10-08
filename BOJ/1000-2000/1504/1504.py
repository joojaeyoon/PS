import sys
import heapq

N, E = map(int, input().split())

edge = [[] for __ in range(N+1)]

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())

    edge[a].append([b, c])
    edge[b].append([a, c])
v1, v2 = map(int, input().split())


def dijkstra(start):
    dp = [sys.maxsize for i in range(N+1)]
    dp[start] = 0

    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        cost, cur = heapq.heappop(heap)

        for e in edge[cur]:
            n_cost = e[1]+cost
            if dp[e[0]] > n_cost:
                dp[e[0]] = n_cost
                heapq.heappush(heap, [n_cost, e[0]])
    return dp


one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)

answer = min(one[v1]+v1_[v2]+v2_[N], one[v2]+v2_[v1]+v1_[N])

print(answer if answer < sys.maxsize else -1)
