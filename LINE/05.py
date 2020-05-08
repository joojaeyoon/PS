
def mkdir(dirs, *args):
    path = args[0][0]

    path = path.split("/")[1:]

    for i in range(len(path)):
        new_path = "/"+"/".join(path[:i+1])
        if new_path not in dirs:
            dirs.append(new_path)

    return dirs


def cp(dirs, *args):
    path = args[0]

    rel_path = "/"+path[0].split("/")[-1]

    longest_path = path[0]

    for d in dirs:
        if path[0] in d[:len(path[0])]:
            longest_path = d if len(d) > len(longest_path) else longest_path

    idx = longest_path.index(rel_path)
    longest_path = longest_path[idx:]

    new_path = path[1]+longest_path
    if path[1] == "/":
        new_path = new_path[1:]

    dirs = mkdir(dirs, [new_path])

    return dirs


def rm(dirs, *args):
    path = args[0][0]

    del_list = []

    for d in dirs:
        if path in d[:len(path)]:
            del_list.append(d)

    for d in del_list:
        dirs.remove(d)

    return dirs


def solution(directory, command):
    commands = {"mkdir": mkdir, "cp": cp, "rm": rm}

    for c in command:
        data = c.split(" ")
        commands[data[0]](directory, data[1:])

    return directory


dr1 = [
    "/",
    "/hello",
    "/hello/tmp",
    "/root",
    "/root/abcd",
    "/root/abcd/etc",
    "/root/abcd/hello"
]

cm1 = [
    "mkdir /root/tmp",
    "cp /hello /root/tmp",
    "rm /hello"
]

dr = [
    "/"
]

cm = [
    "mkdir /a",
    "mkdir /a/b",
    "mkdir /a/b/c",
    "cp /a/b /",
    "rm /a/b/c"
]


solution(dr, cm)
