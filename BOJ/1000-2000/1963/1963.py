from collections import deque

def eratos():
    isPrime=[True for _ in range(10000)]

    isPrime[1]=False

    for i in range(2,5000):
        for j in range(i+i,10000,i):
            isPrime[j]=False
    
    return isPrime

isPrime=eratos()

T=int(input())

for _ in range(T):
    a,b=map(int,input().split())
    answer=10**5

    visited=[False for _ in range(10000)]

    q=deque()

    q.append([a,0])

    while q:
        num,cnt=q.popleft()

        if num==b:
            answer=min(cnt,answer)
            continue
        
        num=str(num)
        for i in range(4):
            for j in range(10):
                if i==0 and j==0:
                    continue
                if str(j)!=num[i]:
                    tmp=int(num[:i]+str(j)+num[i+1:])
                    if isPrime[tmp] and not visited[tmp]:
                        visited[tmp]=True
                        q.append([tmp,cnt+1])

    if answer==10**5:
        print("impossible")
    else:
        print(answer)