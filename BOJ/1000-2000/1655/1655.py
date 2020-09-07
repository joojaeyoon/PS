import sys
import heapq

cnt=int(input())

max_heap=[]
min_heap=[]

for _ in range(cnt):
    data=int(sys.stdin.readline())
    if len(max_heap)==len(min_heap):
        heapq.heappush(max_heap,-data)
    else:
        heapq.heappush(min_heap,data)
    
    if min_heap and -max_heap[0] > min_heap[0]:
        a,b=heapq.heappop(min_heap),heapq.heappop(max_heap)
        heapq.heappush(max_heap,-a)
        heapq.heappush(min_heap,-b)
    
    print(-max_heap[0])
