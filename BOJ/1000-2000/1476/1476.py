answer = list(map(int, input().split()))

years = [1, 1, 1]

limit = [16, 29, 20]

year = 1

while answer != years:
    year += 1

    for i in range(3):
        years[i] += 1
        if years[i] == limit[i]:
            years[i] = 1

print(year)
