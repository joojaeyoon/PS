import sys

N=int(input())
trie={}

for i in range(N):
    data=sys.stdin.readline().split()[1:]
    if not trie.get(data[0]):
        trie[data[0]]={}
    tmp=trie[data[0]]

    for d in data[1:]:
        if not tmp.get(d):
            tmp[d]={}
        tmp=tmp[d]

def printTrie(t,depth):
    if len(t)==0:
        return
    
    for k,v in sorted(t.items()):
        for _ in range(depth):
            print("--",end="")
        print(k)
        printTrie(v,depth+1)

printTrie(trie,0)