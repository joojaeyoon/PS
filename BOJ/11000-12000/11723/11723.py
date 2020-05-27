import sys

N = int(input())

S = [0 for i in range(20)]


def command_all(S):
    for i in range(20):
        S[i] = 1


def command_empty(S):
    for i in range(20):
        S[i] = 0


def command_toggle(S, x):
    if S[x-1] > 0:
        S[x-1] = 0
    else:
        S[x-1] = 1


def command_add(S, x):
    S[x-1] = 1


def command_remove(S, x):
    if S[x-1] > 0:
        S[x-1] = 0


def command_check(S, x):
    if S[x-1] == 1:
        print(1)
    else:
        print(0)


op_func = {
    "add": command_add,
    "remove": command_remove,
    "check": command_check,
    "toggle": command_toggle,
    "all": command_all,
    "empty": command_empty
}

for _ in range(N):
    command = sys.stdin.readline().split()

    if len(command) == 1:
        op_func[command[0]](S)
    else:
        op_func[command[0]](S, int(command[1]))
