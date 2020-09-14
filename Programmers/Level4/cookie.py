# Programmers LV 4 쿠키 구입

def solution(cookie):
    answer = 0

    N=len(cookie)

    if N==1:
        return 0

    for i in range(N-1):

        l_idx,r_idx=i,i+1
        l_sum,r_sum=cookie[i],cookie[i+1]

        while True:

            if l_sum==r_sum:
                answer=max(answer,l_sum)
            
            if l_idx > 0 and l_sum <= r_sum:
                l_idx-=1
                l_sum+=cookie[l_idx]
            elif r_idx < N-1 and l_sum > r_sum:
                r_idx+=1
                r_sum+=cookie[r_idx]
            else:
                break


    return answer

print(solution([1,1,2,3]))
# # solution([1,2,4,5])

