def solution(stones, k):
    answer=0

    lo=0
    hi=200000000

    while lo <= hi:
        
        mid=(lo+hi)>>1

        s=list(stones)

        for i in range(len(s)):
            s[i] -= mid

        seq_minus,max_minus= 0, 0
        
        for i in range(len(s)):
            if s[i]<0:
                seq_minus+=1
                max_minus=max(max_minus,seq_minus)
            else:
                seq_minus=0
        
        if max_minus < k:
            if answer < mid:
                answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
            
    return answer

result=solution([2,4,5,3,2,1,4,2,5,1],3)
print(result==3)