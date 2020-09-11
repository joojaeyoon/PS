# Programmers LV 3 베스트앨범

def solution(genres, plays):
    answer = []

    album = {}
    counter = {}

    for i in range(len(genres)):
        if not album.get(genres[i], False):
            album[genres[i]] = []
        album[genres[i]].append([plays[i], i])

        if not counter.get(genres[i], False):
            counter[genres[i]] = 0
        counter[genres[i]] += plays[i]

    counter = sorted(counter, key=lambda x: counter[x], reverse=True)

    for genre in counter:
        for p in sorted(album[genre], key=lambda x: (x[0], 10000-x[1]), reverse=True)[:2]:
            answer.append(p[1])

    return answer


print(solution(["classic", "pop", "classic",
                "classic", "pop"], [500, 600, 150, 800, 2500]))
