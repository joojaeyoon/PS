n = int(input())
arr = list(map(int, input().split()))

dp = [[arr[i], arr[i]] for i in range(n)]

ans = arr[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0]+arr[i], arr[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+arr[i])
    ans = max(ans, dp[i][0], dp[i][1])

print(ans)
