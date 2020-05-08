from itertools import combinations


def solution(road, n):
    answer = -1

    count = road.count("0")

    if n > count:
        n = count

    combi = combinations([x for x in range(count)], n)

    zero_indice = [i for i, num in enumerate(road) if num == "0"]

    for c in list(combi):
        r = list(road)
        for i in range(n):
            idx = zero_indice[c[i]]
            r[idx] = "1"
        r = "".join(r).split("0")
        length = len(max(r, key=len))
        answer = length if answer < length else answer

    return answer


solution("111011110011111011111100011111", 3)
