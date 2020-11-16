N = int(input())

cow = []
for i in range(N):
    a, b = map(int, input().split())
    cow.append((a, b))
cow.sort()
time = cow[0][0]

for c in cow:
    if time < c[0]:
        time = c[0]
    time += c[1]

print(time)
