import heapq
import sys

heap=[]
cnt=int(input())

for i in range(cnt):
    data=int(sys.stdin.readline())

    if data!=0:
        heapq.heappush(heap,data)
    elif heap:
        print(heapq.heappop(heap))
    else:
        print(0)