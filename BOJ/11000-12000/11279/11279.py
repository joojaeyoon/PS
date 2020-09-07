import heapq
import sys

MAX_NUM=2**31

heap=[]
cnt=int(input())

for _ in range(cnt):
    data=int(sys.stdin.readline())
    
    if data!=0:
        heapq.heappush(heap,MAX_NUM-data)
    elif heap:
        print(MAX_NUM-heapq.heappop(heap))
    else:
        print(0)