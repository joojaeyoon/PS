
T = int(input())


for _ in range(T):
    n = int(input())

    sticker = []

    for __ in range(2):
        sticker.append(list(map(int, input().split())))

    dp = [[0]*n for _ in range(2)]

    for i in range(n):
        dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))
