from collections import deque

N=input()
M=int(input())
broken=[]
if M:
    broken=list(map(int,input().split()))

buttons=[1 if i not in broken else 0 for i in range(10)]

answer=abs(100-int(N))

if M==10:
    print(answer)
else:

    for i in range(1000001):
        flag=True
        for j in str(i):
            if not buttons[int(j)]:
                flag=False
                break
        
        if flag:
            answer=min(answer,len(str(i))+abs(int(N)-i))

    print(answer)