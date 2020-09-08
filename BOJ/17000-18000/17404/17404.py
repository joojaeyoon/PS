import sys

N=int(input())
answer=1000*1000+1

costs=[[] for _ in range(N)]
dp=[[0]*3 for _ in range(N)]

for i in range(N):
    costs[i]=list(map(int,sys.stdin.readline().split()))

for i in range(3):
    
    for j in range(3):
        if i==j:
            dp[0][j]=costs[0][i]
        else:
            dp[0][j]=1000*1000+1

    for j in range(1,N):
        dp[j][0]=min(dp[j-1][1],dp[j-1][2])+costs[j][0]
        dp[j][1]=min(dp[j-1][0],dp[j-1][2])+costs[j][1]
        dp[j][2]=min(dp[j-1][0],dp[j-1][1])+costs[j][2]
    
    for j in range(3):
        if i==j: continue
        answer=min(answer,dp[N-1][j])

print(answer)
