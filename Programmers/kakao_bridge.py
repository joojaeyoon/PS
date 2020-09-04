def solution(stones, k):
    answer = 200000000
    max_value=max(stones[:k])

    for i in range(0,len(stones)-k+1):
        if stones[i-1] == max_value:
            max_value=max(stones[i:i+k])
        if stones[i+k-1] == max_value:
            max_value=stones[i+k-1]

        if answer > max_value:
            answer=max_value
    
    return answer

result=solution([2,4,5,3,2,1,4,2,5,1],3)
print(result==3)