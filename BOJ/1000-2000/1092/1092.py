
N=int(input())
limits=list(map(int,input().split()))
M=int(input())
box=list(map(int,input().split()))

limits.sort(reverse=True)
box.sort(reverse=True)
time=0

deleted=[False for _ in range(M)]
check={l:[] for l in limits}

cnt=0
if box[0] > limits[0]:
    print(-1)
else:
    for l in limits:
        for i in range(M):
            if l >= box[i]:
                check[l].append(i)

    while cnt!=M:
        for l in limits:
            for i in check[l]:
                if not deleted[i]:
                    deleted[i]=True
                    cnt+=1
                    break
        time+=1
            

    print(time)