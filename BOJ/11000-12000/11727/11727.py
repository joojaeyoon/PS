N = int(input())

way = [1, 3]

while len(way) < N:
    way.append((way[-1]+way[-2]*2) % 10007)

print(way[N-1])
