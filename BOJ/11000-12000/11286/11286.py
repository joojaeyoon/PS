import sys
import heapq

cnt=int(input())

heap=[]

for _ in range(cnt):
    data=int(sys.stdin.readline())

    if data!=0:
        heapq.heappush(heap,[abs(data),data])
    else:
        print(heapq.heappop(heap)[1] if heap else 0)