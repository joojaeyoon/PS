import sys
from heapq import heappop, heappush

N = int(input())
classes = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    classes.append((s, e))

classes.sort(key=lambda x: (x[0], x[1]))

heap = [(classes[0][1], classes[0][0])]
for i in range(1, N):
    s, e = classes[i]
    if heap[0][0] <= s:
        heappop(heap)
    heappush(heap, (e, s))

print(len(heap))
