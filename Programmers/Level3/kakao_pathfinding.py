# Programmers LV 3 KAKAO 길 찾기 게임

import sys
sys.setrecursionlimit(10**8)


class Node:
    def __init__(self, x, y, data):
        self.left = None
        self.right = None
        self.x = x
        self.y = y
        self.data = data

    def __repr__(self):
        return str(self.data)


def preorder(node, answer):
    answer[0].append(node.data)
    if node.left != None:
        preorder(node.left, answer)
    if node.right != None:
        preorder(node.right, answer)


def postorder(node, answer):

    if node.left != None:
        postorder(node.left, answer)
    if node.right != None:
        postorder(node.right, answer)

    answer[1].append(node.data)


def solution(nodeinfo):
    answer = [[], []]

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    nodeinfo.sort(key=lambda x: x[1], reverse=True)
    root = None

    for node in nodeinfo:
        x, y, data = node
        newNode = Node(x, y, data)
        if root == None:
            root = newNode
            continue

        tmp = root
        parent = tmp
        while tmp != None:
            parent = tmp
            if x < tmp.x:
                tmp = tmp.left
            else:
                tmp = tmp.right

        if x < parent.x:
            parent.left = newNode
        else:
            parent.right = newNode

    preorder(root, answer)
    postorder(root, answer)

    return answer


# solution([[5, 3], [11, 5], [13, 3], [3, 5], [
#          6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])


solution([[5, 3], [11, 5], [14, 5], [2, 100000], [24, 23], [8, 1292]])
