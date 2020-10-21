import sys
from heapq import heappush, heappop

read = sys.stdin.readline

T = int(input())


def Pop(heap, isMax):
    tmp = heap[0] if heap else sys.maxsize
    if tmp != sys.maxsize and isMax:
        tmp = -tmp

    while tmp != sys.maxsize and counter[tmp] == 0:
        heappop(heap)
        tmp = heap[0] if heap else sys.maxsize
        if tmp != sys.maxsize and isMax:
            tmp = -tmp
    if tmp != sys.maxsize:
        heappop(heap)
        counter[tmp] -= 1

    return tmp


for _ in range(T):

    minHeap = []
    maxHeap = []
    counter = {}

    k = int(input())

    for i in range(k):
        op, n = read().split()
        n = int(n)

        if op == "I":
            if not counter.get(n):
                counter[n] = 0
            counter[n] += 1
            heappush(minHeap, n)
            heappush(maxHeap, -n)
        else:
            if n == 1:
                Pop(maxHeap, 1)
            else:
                Pop(minHeap, 0)

    max_num = Pop(maxHeap, 1)
    if max_num != sys.maxsize:
        counter[max_num] += 1
    min_num = Pop(minHeap, 0)

    if max_num == sys.maxsize or min_num == sys.maxsize:
        print("EMPTY")
    else:
        print(max_num, min_num)
