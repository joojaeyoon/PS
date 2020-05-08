def solution(msg):
    dic = [chr(ord('A')+i) for i in range(-1, 26)]
    a_dict = []
    answer = []

    idx = 0

    while idx < len(msg):
        i = 2
        while msg[idx:idx+i] in a_dict and idx+i <= len(msg):
            i += 1

        if idx+i != len(msg):
            a_dict.append(msg[idx:idx+i])
        elif msg[idx:idx+i] in a_dict:
            answer.append(27+a_dict.index(msg[idx:idx+i]))
            break

        if i == 2:
            answer.append(dic.index(msg[idx:idx+i-1]))
        else:
            answer.append(27+a_dict.index(msg[idx:idx+i-1]))
            idx += i-2

        idx += 1

    print(answer)

    return answer


if __name__ == "__main__":

    # solution("ABABABABABABABAB")
    solution("TOBEORNOTTOBEORTOBEORNOT")
