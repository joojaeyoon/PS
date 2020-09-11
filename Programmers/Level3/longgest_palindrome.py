# Programmers LV 3 가장 긴 팰린드롬

def check(s):
    
    for i in range(len(s)//2):
        if s[i]!=s[-1-i]:
            return False
    return True

def solution(s):
    answer=-1
    start,end=0,0

    while start<len(s):

        if end-start+1 < answer:
            end+=1
            continue
        
        if check(s[start:end]):
            answer=max(answer,len(s[start:end]))
        end+=1
        if end>len(s):
            start+=1
            end=start+1

    return answer

r=solution("abcdcba")
# r=solution("abacde")

print(r)