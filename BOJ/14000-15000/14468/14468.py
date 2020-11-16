path = input()
check = {}
answer = 0

for i in range(52):
    if not check.get(path[i]):
        check[path[i]] = []

    check[path[i]].append(i)


for i in range(26):
    a = chr(i+ord("A"))
    for j in range(26):
        if i == j:
            continue
        b = chr(j+ord("A"))

        x1, x2 = check[a]
        x3, x4 = check[b]

        if x1 < x3 and x3 < x2 and x2 < x4:
            answer += 1
print(answer)
