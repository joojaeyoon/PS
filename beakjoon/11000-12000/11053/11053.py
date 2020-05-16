A = int(input())

arr = list(map(int, input().split()))

dp = [0 for _ in range(A)]

dp[0] = 1

for i in range(1, A):
    m = 0
    for j in range(i):
        if arr[i] > arr[j]:
            m = max(m, dp[j])
    dp[i] = m+1

print(max(dp))
