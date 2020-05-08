heights = [int(input()) for i in range(9)]


def select(h, count, last, selected):

    if count == 0 and sum(selected) == 100:
        for i in sorted(selected):
            print(i)
        exit()

    for i in range(last+1, len(h)):
        select(h, count-1, i, selected+[h[i]])


select(heights, 7, -1, [])
