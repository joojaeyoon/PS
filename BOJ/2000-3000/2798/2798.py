from itertools import combinations

N,M=map(int,input().split())

cards=list(map(int,input().split()))
answer=-10**8

nums=[sum(comb) for comb in combinations(cards,3)]

for n in nums:
    if n <= M and M-n < M-answer:
        answer=n

print(answer)