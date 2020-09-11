n,m = map(int,input().split())

num=[True for _ in range(m-n+1)]
count=0
N=1

while N*N <= m:
    N+=1
    square=N*N
    i=n//square

    while square * i <= m:
        idx = square * i - n

        if idx>=0 and num[idx]:
            count+=1
            num[idx]=False
        i+=1

print(len(num)-count)