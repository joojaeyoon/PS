def solution(clothes):
    answer = 1
    counter = {}
    for c in clothes:
        if not counter.get(c[1], False):
            counter[c[1]] = 0
        counter[c[1]] += 1

    for i, v in enumerate(counter.values()):
        answer *= (v+1)
    answer -= 1

    return answer


print(solution([["yellow_hat", "headgear"],
                ["blue_sunglasses", "eyewear"],
                ["green_turban", "headgear"]]))

print(solution([["crow_mask", "face"],
                ["blue_sunglasses", "face"],
                ["smoky_makeup", "face"]]))
