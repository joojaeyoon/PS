# Programmers LV 3 이중우선순위큐

import heapq

def solution(operations):
    heap=[]

    for op in operations:
        cmd,data=op.split()
        data=int(data)

        if cmd=="I":
            heapq.heappush(heap,data)
        elif len(heap)!=0:
            if data==1:
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)
    if len(heap)==0:
        return [0,0]
    
    print(heap)
    return [max(heap),heap[0]]


r=solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
print(r)