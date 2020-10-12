import sys

N = int(input())
answer = 0
nega = []
posi = []

zero = False

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        zero = True
    elif num == 1:
        answer += num
        continue

    if num > 0:
        posi.append(num)
    else:
        nega.append(num)

posi.sort()
nega.sort(reverse=True)

arr = [nega, posi]

for i, a in enumerate(arr):
    while len(a) > 1:
        n1 = a.pop()
        n2 = a.pop()

        answer += n1*n2
    if i == 0 and a and zero:
        continue
    if a:
        answer += a[0]

print(answer)
