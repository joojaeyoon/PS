import sys
from heapq import heappop, heappush, heapify

N, K = map(int, input().split())
answer = 0

gem = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline()) for _ in range(K)]

gem.sort(key=lambda x: x[0])
bag.sort()

heap = []
idx = 0
for b in bag:
    while idx < N and gem[idx][0] <= b:
        heappush(heap, -gem[idx][1])
        idx += 1

    if heap:
        answer += -heappop(heap)
print(answer)
