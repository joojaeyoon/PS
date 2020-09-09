import sys

N=int(input())
people=[]
rank=[1 for i in range(N)]

for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    people.append([a,b])

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if people[i][0] > people[j][0] and \
            people[i][1] > people[j][1]:
            rank[j]+=1

print(*rank)