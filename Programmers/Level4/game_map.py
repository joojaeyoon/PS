# Programmers LV 4 게임 맵 최단거리

from collections import deque

def solution(maps):
    answer = 0

    n,m=len(maps[0]),len(maps)

    visited=[[10**4 for __ in range(n)]for _ in range(m)]

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    q=deque()

    q.append([0,0,1])

    visited[0][0]=1

    while q:

        x,y,cost=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0 <= nx and nx < n and\
                0 <= ny and ny < m and\
                    maps[ny][nx]==1 and\
                        visited[ny][nx] > visited[y][x]+1:
                    
                    q.append([nx,ny,cost+1])
                    visited[ny][nx]=cost+1
    answer = visited[-1][-1] if visited[-1][-1]!=10**4 else -1

    return answer


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])