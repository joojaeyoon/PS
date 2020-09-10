T=input()
P=input()

cnt=0
pos=[]

def getPi(p):
    j=0
    pi=[0 for _ in range(len(p))]

    for i in range(1,len(p)):
        while j>0 and p[i] != p[j]:
            j=pi[j-1]
        if p[i]==p[j]:
            pi[i]=j+1
            j+=1

    return pi

def kmp(t,p):
    ans=[]
    pi=getPi(p)
    n=len(t)
    m=len(p)
    j=0

    for i in range(n):
        while j > 0 and t[i] != p[j]:
            j=pi[j-1]
        if t[i]==p[j]:
            if j==m-1:
                ans.append(i-m+2)
                j=pi[j]
            else:
                j+=1
    return ans

ans=kmp(T,P)

print(len(ans))
print(*ans)