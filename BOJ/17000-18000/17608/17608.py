import sys

N = int(input())

heights = []

for _ in range(N):
    heights.append(int(sys.stdin.readline()))

h = heights[-1]
count = 1

for i in range(N-1, -1, -1):
    if heights[i] > h:
        count += 1
        h = heights[i]

print(count)
