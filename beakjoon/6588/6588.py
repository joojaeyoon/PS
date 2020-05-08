import sys

isPrime = [True for _ in range(1000001)]


for i in range(2, len(isPrime)):
    if isPrime[i]:
        for j in range(i+i, len(isPrime), i):
            isPrime[j] = False

while True:
    num = int(sys.stdin.readline())

    if num == 0:
        break

    for i in range(3, int(num/2)+1, 2):
        if isPrime[i] and isPrime[num-i]:
            print("{0} = {1} + {2}".format(num, i, num-i))
            break
