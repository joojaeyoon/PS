N = int(input())

way = [1, 2]


while len(way) < N:
    way.append((way[-1]+way[-2]) % 10007)

print(way[N-1])
