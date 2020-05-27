A = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(A)]
dp2 = [arr[i] for i in range(A)]

ans = dp2[0]

for i in range(A):
    for j in range(i):
        if arr[i] > arr[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
            dp2[i] = max(dp2[i], dp2[j]+arr[i])
        ans = max(ans, dp2[i])

print(ans)
