N=int(input())

def isPalindrome(word):
    l=len(word)
    for i in range((l>>1)+1):
        if word[i] != word[l-i-1]:
            return False
    return True

def isPrime(num):

    if num==1:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True

while True:
    
    if isPalindrome(str(N)) and isPrime(N):
        print(N)
        break
    N+=1