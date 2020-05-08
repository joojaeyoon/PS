class Message:
    def __init__(self, data):
        data = data.split(" ")
        if len(data) == 2:
            data.append("None")
        self.uid = data[1]
        self.name = data[2]
        self.state = data[0]
        self.changed = False

    def __repr__(self):
        if state == "Enter":
            return self.name+"님이 들어왔습니다."
        elif state == "Leave":
            return self.name+"님이 나갔습니다."


def solution(record):
    answer = []

    log = []

    for r in record:
        log.append(Message(r))

    log = log[::-1]

    for i in range(len(log)-1):
        for j in range(i+1, len(log)):
            if log[j].uid == log[i].uid and not log[j].changed:
                log[j].name = log[i].name

    answer = log[::-1]

    return answer


a = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
     "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

solution(a)
