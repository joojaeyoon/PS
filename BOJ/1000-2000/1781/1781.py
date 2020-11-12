import sys
from heapq import heappop, heappush

N = int(input())
ramen = []
heap = []
answer = 0

for _ in range(N):
    day, cost = map(int, sys.stdin.readline().split())
    ramen.append((day, cost))

ramen.sort()
for i in range(N):
    day, cost = ramen[i]

    heappush(heap, cost)

    while day < len(heap):
        heappop(heap)

while heap:
    answer += heappop(heap)

print(answer)
