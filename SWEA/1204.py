T = int(input())

for i in range(T):
    N = int(input())
    num = 0
    value = 0

    counter = {i: 0 for i in range(101)}

    for n in map(int, input().split()):
        counter[n] += 1

    for k, v in counter.items():
        if v >= value:
            value = v
            num = k

    print(f"#{N} {num}")
