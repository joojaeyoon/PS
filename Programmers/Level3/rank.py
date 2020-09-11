# Programmers LV 3 순위

from collections import defaultdict

def solution(n, results):
    answer = 0
    win=defaultdict(set)
    lose=defaultdict(set)

    for r in results:
        win[r[0]].add(r[1])
        lose[r[1]].add(r[0])

    for i in range(1,n+1):
        for w in win[i]:
            lose[w].update(lose[i])
        for l in lose[i]:
            win[l].update(win[i])
    
    for i in range(1,n+1):
        if len(lose[i])+len(win[i])==n-1:
            answer+=1
            
    return answer

result=solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

print(result==2)