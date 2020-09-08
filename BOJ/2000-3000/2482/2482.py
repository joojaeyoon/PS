# 2482 색상환

N=int(input())
K=int(input())

mod=10**9+3

dp=[[0 for j in range(i+1)] for i in range(N+1)]

for i in range(1,4):
    dp[i][1]=i

for i in range(4,N+1):
    for j in range(1,int(i/2)+1):
        if j==1: dp[i][j]=i
        else:
            dp[i][j] = (dp[i-2][j-1] + dp[i-1][j]) % mod

print(dp[N][K])