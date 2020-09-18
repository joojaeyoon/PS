# Programmers LV 4 스티커 모으기(2)

def solution(sticker):
    answer = 0

    N=len(sticker)

    if N==1:
        return sticker[0]
    elif N==2:
        return max(sticker)
    elif N==3:
        return max(sticker[0]+sticker[2],sticker[1])

    dp=[[0 for _ in range(N)]for __ in range(2)]

    dp[0][0]=sticker[0]
    dp[0][1]=dp[0][0]
    dp[0][2]=dp[0][0]+sticker[2]
    
    dp[1][1]=sticker[1]
    dp[1][2]=max(sticker[1],sticker[2])
    dp[1][3]=dp[1][1]+sticker[3]

    for i in range(3,N-1):
        dp[0][i]=max(dp[0][i-1],dp[0][i-3]+sticker[i],dp[0][i-2]+sticker[i])

    for i in range(3,N):
        dp[1][i]=max(dp[1][i-1],dp[1][i-3]+sticker[i],dp[1][i-2]+sticker[i])
    
    answer=max(dp[0][-2],dp[1][-1])

    return answer

solution([1,3,2,5,4])
solution([14,6,5,11,3,9,2,10])