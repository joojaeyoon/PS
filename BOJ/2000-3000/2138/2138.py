N = int(input())

cur = list(map(int, list(input())))
cur2 = cur.copy()
target = input()
cur2[0] ^= 1
cur2[1] ^= 1

flag = False
count = 10**8

for idx, c in enumerate([cur, cur2]):
    cnt = 0
    for i in range(1, N):
        if c[i-1] != int(target[i-1]):
            c[i-1] ^= 1
            c[i] ^= 1
            if i+1 < N:
                c[i+1] ^= 1
            cnt += 1

    s = "".join(map(str, c))

    if idx == 1:
        cnt += 1

    if s == target:
        flag = True
        count = min(count, cnt)

if flag:
    print(count)
else:
    print(-1)
