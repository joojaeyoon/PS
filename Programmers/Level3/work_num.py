# Programmers LV 3 야근 지수

import heapq

def solution(n, works):
    answer = 0

    for i in range(len(works)):
        works[i]=-works[i]
    
    heapq.heapify(works)

    for _ in range(n):
        value=heapq.heappop(works)
        if value==0:
            break
        value=-value-1
        heapq.heappush(works,-value)
    
    for w in works:
        answer+=w**2
    
    return answer

r=solution(4,[4,3,3])
r=solution(1,[2,1,2])
r=solution(3,[1,1])
print(r)