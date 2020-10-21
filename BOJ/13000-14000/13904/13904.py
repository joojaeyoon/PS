N = int(input())

hw = [list(map(int, input().split())) for _ in range(N)]
check = [0 for _ in range(1001)]
answer = 0

hw.sort(key=lambda x: -x[1])
for d, w in hw:
    idx = d
    while idx != 0 and check[idx]:
        idx -= 1
    if idx != 0:
        check[idx] = 1
        answer += w

print(answer)
