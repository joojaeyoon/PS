S = input()

counter = [0, 0]
check = S[0]

counter[int(check)] += 1

for c in S:
    if c == check:
        continue
    else:
        check = c
        counter[int(check)] += 1

print(min(counter))
