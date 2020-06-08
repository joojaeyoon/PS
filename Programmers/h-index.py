def solution(citations):

    if min(citations) >= len(citations):
        return len(citations)

    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] <= i:
            break

    return i


print(solution([3, 0, 6, 1, 5]))
