N,M=map(int,input().split())
pos=list(map(int,input().split()))

answer=0

pos.sort()

positive=[]
negative=[]

maxp,maxn=-1,-1

for p in pos:
    if p >0:
        positive.append(p)
        maxp=max(maxp,p)
    else:
        negative.append(p)
        maxn=min(maxn,p)

for i in range(len(positive)-1,-1,-M):
    answer+=positive[i]*2
for i in range(0,len(negative),M):
    answer+=abs(negative[i])*2

maxP=max(maxp,abs(maxn))
answer-=maxP
    
print(answer)