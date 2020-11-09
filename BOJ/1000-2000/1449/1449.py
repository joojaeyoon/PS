N, L = map(int, input().split())

pos = sorted(list(map(int, input().split())))
answer = 0

i = 0
while i < N:
    r = pos[i]-0.5
    j = i+1
    while j < N:
        if pos[j]+0.5 > r+L:
            break
        j += 1

    i = j
    answer += 1

print(answer)
