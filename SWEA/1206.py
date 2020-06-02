

for i in range(10):
    n = int(input())

    B = list(map(int, input().split()))
    count = 0

    for j in range(2, len(B)-2):
        a, b, c, d = B[j-2], B[j-1], B[j+1], B[j+2]

        result = B[j]-max(a, b, c, d)

        if result > 0:
            count += result

    print(f"#{i+1} {count}")
