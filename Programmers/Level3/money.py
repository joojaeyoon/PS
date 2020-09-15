# Programmers LV 3 거스름돈

def solution(n, money):
    mod=1000000007

    dp=[0 for _ in range(n+1)]
    dp[0]=1

    for i in range(len(money)):
        for j in range(n+1):
            if j >= money[i]:
                dp[j]=(dp[j]+dp[j-money[i]])%mod
    return dp[-1]

solution(5,[1,2,5])