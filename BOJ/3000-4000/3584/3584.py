import sys

T=int(input())

def getParent(edge,li,start):
    idx=start
    li.append(idx)

    while edge[idx]!=-1:
        li.append(edge[idx])
        idx=edge[idx]


for _ in range(T):
    N=int(input())
    edge=[-1 for _ in range(N+1)]

    for __ in range(N-1):
        A,B=map(int,sys.stdin.readline().split())
        edge[B]=A
    A,B=map(int,sys.stdin.readline().split())
    
    parent_A=[]
    parent_B=[]
    
    getParent(edge,parent_A,A)
    getParent(edge,parent_B,B)

    answer=-1

    while parent_A and parent_B and parent_A[-1]==parent_B[-1]:
        answer=parent_A[-1]
        parent_A.pop()
        parent_B.pop()
    
    print(answer)