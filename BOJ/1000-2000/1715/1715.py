import sys
from heapq import heappush, heappop

N = int(input())
answer = 0

heap = []

for _ in range(N):
    heappush(heap, int(sys.stdin.readline()))

while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)

    heappush(heap, a+b)
    answer += a+b

print(answer)
