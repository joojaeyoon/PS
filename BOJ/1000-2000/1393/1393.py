x,y=map(int,input().split())
tx,ty,mx,my=map(int,input().split())

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

g=gcd(mx,my)

mx,my=int(mx/g),int(my/g)

distance=10**8

ax,ay=0,0

while tx <= 100 and ty <= 100:
    d=(x-tx)**2+(y-ty)**2

    if d < distance:
        distance=d
        ax,ay=tx,ty

    tx+=mx
    ty+=my

print(ax,ay)