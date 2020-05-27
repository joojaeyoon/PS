import sys

T = int(input())

way = [1, 2, 4]

for _ in range(T):
    n = int(input())

    while len(way) < n:
        way.append((way[-1]+way[-2]+way[-3]) % 1000000009)

    print(way[n-1])
