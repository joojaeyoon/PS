N = int(input())
arr = list(map(int, input().split()))
answer = 0

dp = [0 for _ in range(N+1)]
mx = 0

for i in range(N):
    dp[arr[i]] = dp[arr[i]-1]+1
    mx = max(mx, dp[arr[i]])

print(N-mx)
