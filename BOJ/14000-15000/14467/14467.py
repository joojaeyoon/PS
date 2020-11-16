N = int(input())
check = {}
answer = 0

for _ in range(N):
    a, b = map(int, input().split())

    if check.get(a, None) != None:
        if check[a] != b:
            check[a] = b
            answer += 1
    else:
        check[a] = b

print(answer)
