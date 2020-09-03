def is_prime(num):
    if num in (0,1):
        return False
    
    for i in range(2,num//2):
        if num%i==0:
            return False

    return True

def select(num,numbers,visited,toPick,prime):
    if toPick==0:
        print(int(num))
        if is_prime(int(num)): prime.add(int(num))
        return
    
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i]=True
            select(num+numbers[i],numbers,visited,toPick-1,prime)
            visited[i]=False

def solution(numbers):
    answer = 0
    numbers=list(numbers)
    visited=[False for i in range(len(numbers))]
    prime=set()
    
    for i in range(1,len(numbers)+1):
        select("",numbers,visited,i,prime)

    answer=len(prime)

    return answer

result=solution("17")
print(result==3)

# result=solution("011")
# print(result==2)