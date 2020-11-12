T = int(input())

for _ in range(T):
    cost = int(input())
    money = [1, 10, 25]
    answer = 0
    dp = [i for i in range(101)]

    for i in range(1, 100):
        for j in money:
            if i-j >= 0:
                dp[i] = min(dp[i], dp[i-j]+1)

    while cost:
        c = cost % 100

        answer += dp[c]
        cost = int(cost/100)

    print(answer)
