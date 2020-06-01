import heapq


def solution(scoville, K):
    answer = 0

    h = []

    for s in scoville:
        heapq.heappush(h, (s, 0))

    while h[0][0] < K:
        if len(h) < 2:
            return -1

        a, b = heapq.heappop(h)[0], heapq.heappop(h)[0]

        new_scoville = a+b*2

        heapq.heappush(h, (new_scoville, new_scoville))

        answer += 1

    return answer


result = solution([1, 2, 3, 9, 10, 12], 7)

print(result)
