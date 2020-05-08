def seperate(m):
    ret = ""

    print(m)
    m = list(m)
    print(m)

    for i in range(len(m)-1):
        ret += m[i]
        if m[i+1] != "#":
            ret += " "
    ret += m[-1]

    print(ret)

    return ret+" "


def getInfo(info):
    info = info.split(",")
    start_time = info[0].split(":")
    end_time = info[1].split(":")

    time = (int(end_time[0])-int(start_time[0]))*60 + \
        int(end_time[1])-int(start_time[1])

    while len(info[3]) < time:
        info[3] += info[3]
    info[3] = seperate(info[3][:time])

    info = [time, info[2], info[3]]

    return info


def solution(m, musicinfos):
    answer = []

    m = seperate(m)

    for i in range(len(musicinfos)):
        musicinfos[i] = getInfo(musicinfos[i])

        if m in musicinfos[i][2]:
            answer.append(musicinfos[i])

    if len(answer) == 0:
        return "(None)"

    answer = sorted(answer, key=lambda x: (len(x[1]), x[0]))

    return answer[-1][1]


mi = ["13:00,13:15,WORLD,ABA#B#C#D#F#"]

print(solution("A#B#C#D#F#", mi))

# print(seperate("ABC#DE#FG"))
