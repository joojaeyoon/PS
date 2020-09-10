N,M=map(int,input().split())
arr=list(map(int,input().split()))

answer=0

start=0
end=1

while start!=len(arr):
    s=sum(arr[start:end])

    if s == M:
        answer+=1
        start+=1
        end=start+1
    elif s < M and end != len(arr):
        end+=1
    else:
        start+=1
    
    if start>end:
        end+=1

print(answer)
