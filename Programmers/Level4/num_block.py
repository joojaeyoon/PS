# Programmers LV 4 숫자 블록

from math import sqrt

def getD(num):

    if num==1:
        return 0

    for i in range(2,int(sqrt(num))+1):
        if num%i==0 and num/i <= 10**7:
            return int(num/i)
    return 1

def solution(begin, end):
    answer = []

    for i in range(begin,end+1):
        answer.append(getD(i))

    return answer


solution(1,10)