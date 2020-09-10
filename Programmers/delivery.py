from collections import deque

def solution(N, road, K):
    answer = 0
    visited=[500001 for _ in range(N+1)]
    
    edge=[[] for _ in range(N+1)]

    for r in road:
        edge[r[0]].append([r[1],r[2]])
        edge[r[1]].append([r[0],r[2]])
    
    q=deque()

    q.append([1,0])
    visited[1]=0

    while q:
        cur,cost=q.popleft()

        for r in edge[cur]:
            new_cost=cost+r[1]
            if visited[r[0]] > new_cost:
                visited[r[0]] = new_cost
                q.append([r[0],new_cost])
    for v in visited:
        if v <= K:
            answer+=1

    return answer

r=solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)
r=solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4)
print(r)