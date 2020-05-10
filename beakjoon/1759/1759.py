
L, C = list(map(int, input().split()))
alpha = input().split()
alpha.sort()


def select(selected, toPick, prev, mo, ja):
    if toPick == 0 and mo >= 1 and ja >= 2:
        print(selected)
        return

    for i in range(prev+1, len(alpha)):

        if alpha[i] in ("a", "e", "i", "o", "u"):
            select(selected+alpha[i], toPick-1, i, mo+1, ja)
        else:
            select(selected+alpha[i], toPick-1, i, mo, ja+1)


select("", L, -1, 0, 0)
