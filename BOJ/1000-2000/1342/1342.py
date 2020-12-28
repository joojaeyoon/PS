from collections import Counter
import math

S = sorted(list(input()))

counter = Counter(S)
answer = 0
total = len(S)

if len(counter) == len(S):
    print(math.factorial(len(S)))
    exit(0)


def next_permutation(a):
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i+1]):
        i -= 1
    if i < 0:
        return False
    j = len(a) - 1
    while not (a[j] > a[i]):
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i+1:] = reversed(a[i+1:])
    return True


def check(s):
    flag = True
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            flag = False
            break
    if flag:
        global answer
        answer += 1


check(S)
while next_permutation(S):
    check(S)

print(answer)
