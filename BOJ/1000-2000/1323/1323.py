N,K=map(int,input().split())

first=N-int(N/K)*K
check={first:1}

cnt=1
flag=True
tmp=N
L=10**len(str(N))

while tmp % K:
    tmp=tmp*L+N
    tmp=tmp-int(tmp/K)*K

    if check.get(tmp):
        flag=False
        break
    check[tmp]=1
    cnt+=1

if flag:
    print(cnt)
else:
    print(-1)
    