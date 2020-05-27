
N = int(input())
P = list(map(int, input().split()))

dp = P.copy()+[10000000000]


for i in range(N):
    for j in range(i+1):
        dp[i] = min(dp[i-j-1]+P[j], dp[i])

print(dp[N-1])
