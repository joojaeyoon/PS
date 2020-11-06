from collections import Counter

N, K = map(int, input().split())
order = list(map(int, input().split()))
counter = Counter(order)
answer = 0
isin = {i: False for i in range(1, K+1)}
tab = []

i = 0
while len(tab) < N and i < K:
    if not isin[order[i]]:
        isin[order[i]] = True
        tab.append(order[i])
    counter[order[i]] -= 1
    i += 1

for i in range(i, len(order)):
    val = order[i]

    if isin[val]:
        counter[val] -= 1
        continue

    tmp = 0

    for j in range(1, N):
        a, b = tab[tmp], tab[j]
        if counter[a] >= counter[b]:
            tmp = j
    tmp = tab[tmp]

    if counter[tmp] != 0:
        check = {i: False for i in range(1, K+1)}
        for j in range(i+1, len(order)):
            if isin[order[j]] and not check[order[j]]:
                tmp = order[j]
                check[order[j]] = True
    idx = tab.index(tmp)

    tab[idx] = val
    counter[val] -= 1
    isin[tmp] = False
    isin[val] = True
    answer += 1

print(answer)
