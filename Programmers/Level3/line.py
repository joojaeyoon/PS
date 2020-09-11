# Programmers LV 3 줄 서는 방법

def solution(n, k):
    answer = []

    numbers=[i for i in range(1,n+1)]

    fac=1

    for i in range(2,n+1):
        fac*=i

    while n!=0:
        fac=int(fac/n)
        
        N=int((k-1)/fac)
        k%=fac
        if k==0:
            k=fac
        n-=1
        answer.append(numbers[N])
        numbers.pop(N)
    
    print(answer)
    return answer

r=solution(3,1)
r=solution(3,2)
r=solution(4,6)