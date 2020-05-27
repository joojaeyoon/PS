n = int(input())
arr = list(map(int, input().split()))

dp = [arr[i] for i in range(n)]

ans = dp[0]

for i in range(1, n):
    if dp[i-1]+arr[i] > arr[i]:
        dp[i] = dp[i-1]+arr[i]
print(max(dp))
