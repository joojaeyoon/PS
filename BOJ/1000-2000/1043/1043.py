def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])


def union(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

truth = list(map(int, input().split()))[1:]
party = []

answer = 0

parent = [i for i in range(N+1)]

for i in range(len(truth)-1):
    union(parent, truth[i], truth[i+1])

for i in range(M):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        answer += 1
        continue
    party.append(tmp[1:])

    for i in range(1, len(tmp)-1):
        union(parent, tmp[i], tmp[i+1])

for p in party:
    flag = True
    for i in range(len(truth)):
        if getParent(parent, p[0]) == getParent(parent, truth[i]):
            flag = False
            break
    if flag:
        answer += 1

print(answer)
