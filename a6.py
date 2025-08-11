from builtins import int, len, list, map, print, range, sorted, str
import sys

def relabel(n, adj, theNode):
    mapping = {}
    newAdj = [[] for _ in range(n - 1)]

    for old in range(n):
        if old != theNode:
            newLabel = len(mapping)
            mapping[old] = newLabel

    for oldU in range(n):
        if oldU != theNode:
            newU = mapping[oldU]
            for oldV in adj[oldU]:
                if oldV != theNode:
                    newV = mapping[oldV]
                    newAdj[newU].append(newV)

    for a in newAdj:
        a.sort()

    return len(newAdj), newAdj

def reverse(n, adj):
    revAdj = [[] for _ in range(n)]
    
    for u in range(n):
        for v in adj[u]:
            if v < n: 
                revAdj[v].append(u)

    for i in range(n):
        revAdj[i] = sorted(revAdj[i])

    return revAdj

inputLines = sys.stdin.read().strip().split('\n')
dgs = []
index = 0

while index < len(inputLines):
    line = inputLines[index].strip()
    if line == "0":
        break
    elif line:
        n = int(line)
        adj = []
        for _ in range(n):
            index += 1
            if index < len(inputLines):
                adjLine = inputLines[index].strip()
                adj.append(list(map(int, adjLine.split())) if adjLine else [])
        dgs.append((n, adj))
    index += 1

output = []

for n, adj in dgs:
    delNode = n - 3
    newN, newAdj = relabel(n, adj, delNode)
    revAdj = reverse(newN, newAdj)
    
    output.append(str(newN))
    for a in revAdj:
        output.append(' '.join(map(str, a)) if a else '')

for line in output:
    print(line)

print('0')
