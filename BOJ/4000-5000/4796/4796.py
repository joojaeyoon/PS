
i = 1
while True:
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        exit(0)

    answer = 0

    answer += int(V/P)*L
    V -= P*int(V/P)

    if L > V:
        answer += V
    else:
        answer += L

    print(f"Case {i}: {answer}")
    i += 1
