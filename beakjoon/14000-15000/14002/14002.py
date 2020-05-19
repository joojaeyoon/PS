A = int(input())

arr = list(map(int, input().split()))

dp = [1 for _ in range(A)]

indice = [-1 for _ in range(A)]

for i in range(A):
    for j in range(i):
        if arr[i] > arr[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
            indice[i] = j

idx = 0
ans = []
for i in range(len(dp)):
    idx = i if dp[i] > dp[idx] else idx

print(dp[idx])

ans.append(arr[idx])
idx = indice[idx]

while idx >= 0:
    ans.append(arr[idx])
    idx = indice[idx]

print(*ans[::-1])
