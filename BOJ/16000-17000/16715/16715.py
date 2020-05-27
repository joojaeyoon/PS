

def getN(num, N):
    total = 0

    while num > 1:

        tmp = num % N
        num = int(num/N)
        total += tmp

    total += num

    return total


N = int(input())


high = 0
high_idx = 0

for i in range(2, N+1):
    result = getN(N, i)
    if result > high:
        high = result
        high_idx = i

print(high, high_idx)
