from collections import deque

N=int(input())

dp=[]

q=deque([i for i in range(10)])

while len(dp) < 1023:
    n=q.popleft()
    dp.append(n)

    last=n%10

    for i in range(last):
        q.append(n*10+i)

if N > 1022:
    print(-1)
else:
    print(dp[N])
    


