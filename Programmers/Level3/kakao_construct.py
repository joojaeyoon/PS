# Programmers LV 3 경주로 건설

from collections import deque

def solution(board):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    directions=[2,6,8,4]
    
    N=len(board)

    visited=[[[25**2*500,25*25] for _ in range(N)] for __ in range(N)]
    visited[0][0]=[0,0]
    q=deque()

    q.append([0,0,0,-1,0])

    while q:
        x,y,cost,direct,corner=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            tmp_cost=cost
            tmp_corner=corner
            if 0 <= nx and nx < N and 0 <= ny and ny < N and \
                board[ny][nx]!=1:
                
                if direct==-1 or direct==directions[i]:
                    tmp_cost+=100
                elif direct!=directions[i]:
                    tmp_cost+=600
                    tmp_corner+=1

                if visited[ny][nx][0] >= tmp_cost:
                    visited[ny][nx][0] = tmp_cost
                    visited[ny][nx][1] = min(visited[ny][nx][1],tmp_corner)
                    q.append([nx,ny,tmp_cost,directions[i],tmp_corner])

    return visited[-1][-1][0]

# result=solution([[0,0,0],[0,0,0],[0,0,0]])
result=solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
# result=solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
# result=solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])

print(result)
