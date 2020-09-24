# Programmers LV 4 2018 KAKAO BLIND 자동 완성

def check(w1, w2):
    cnt = 0

    i = 0

    while i < len(w1) and i < len(w2):
        if w1[i] != w2[i]:
            break
        cnt += 1
        i += 1

    if i != len(w1):
        cnt += 1

    return cnt


def solution(words):
    answer = 0

    words.sort()

    for i in range(len(words)):
        tmp = 0
        if i != 0:
            tmp = check(words[i], words[i-1])
        if i != len(words)-1:
            tmp = max(check(words[i], words[i+1]), tmp)
        answer += tmp

    return answer


solution(["abc", "def", "ghi", "jklm"])
solution(["word", "war", "warrior", "world"])
solution(["go", "gone", "guild"])
