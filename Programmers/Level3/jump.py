# Programmers LV 3 멀리 뛰기

def solution(n):
    dp=[1,2]

    while len(dp) < n:
        dp.append((dp[-1]+dp[-2])%1234567)

    return dp[n-1]

solution(4)
# solution(3)