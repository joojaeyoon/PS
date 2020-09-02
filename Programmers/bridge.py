
def solution(distance, rocks, n):
    answer = distance
    dists=[]

    rocks.sort()
    rocks.append(distance)

    dists.append(rocks[0])
    for i in range(len(rocks)-1):
        dists.append(rocks[i+1]-rocks[i])
    
    start=0
    end=distance

    while start<=end:
        cnt=0
        accu=0
        mid=(start+end)>>1
        
        for d in dists:
            if d+accu<mid:
                cnt+=1
                accu+=d
            else:
                accu=0
        if cnt > n:
            end=mid-1
        else:
            start=mid+1
            answer=mid
    
    return answer


result=solution(25,[2,14,11,21,17],2)
print(result)

result=solution(16,[4,8,11],2)
print(result)
