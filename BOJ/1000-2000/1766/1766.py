import sys
from heapq import heappop, heappush

N, M = map(int, input().split())

edge = [[] for _ in range(N+1)]
pre_cnt = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    pre_cnt[b] += 1

heap = []

for i in range(1, N+1):
    if pre_cnt[i] == 0:
        heappush(heap, i)

for _ in range(N):

    x = heappop(heap)
    print(x, end=" ")

    for e in edge[x]:
        pre_cnt[e] -= 1
        if pre_cnt[e] == 0:
            heappush(heap, e)

print()
