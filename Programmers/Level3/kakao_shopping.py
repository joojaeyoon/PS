# Programmers LV 3 보석 쇼핑

from collections import Counter

def solution(gems):
    answer=[0,len(gems)+1]
    counter=Counter(gems)
    size=len(counter)

    start,end=0,0

    counter={}
        
    while start != len(gems):
        s=len(counter)

        if s < size:
            if end==len(gems):
                break
            key=gems[end]
            if not counter.get(key):
                counter[key]=0
            counter[key]+=1
            end+=1
        elif s == size:
            while len(counter) == size:
                
                key=gems[start]
                start+=1

                if counter.get(key)==1:
                    counter.pop(key)
                else:
                    counter[key]-=1

            if end-start < answer[1]-answer[0]:
                answer= [start,end]
            
            counter={}
            end=start
    
    return answer
        

# r=solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
# r=solution(["AA", "AB", "AC", "AA", "AC"])
# r=solution(["XYZ", "XYZ", "XYZ"])
# r=solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
r=solution(["DIA", "EM", "EM", "RUB", "DIA"])

print(r)