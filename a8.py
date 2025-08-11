from collections import deque
import sys

def bfs(s, t, g, n):
    d = [n] * n
    d[s] = 0
    q = deque([s])
    
    while q:
        u = q.popleft()
        for v in g[u]:
            if d[v] == n:
                d[v] = d[u] + 1
                q.append(v)
                
    return d[t]

inputLines = sys.stdin.read().strip().split('\n')
idx = 0

while idx < len(inputLines):
    n = int(inputLines[idx].strip())
    if n == 0:
        break
    idx += 1
    g = [[] for _ in range(n)]
    
    for i in range(n):
        adj = list(map(int, inputLines[idx].strip().split()))
        g[i].extend(adj)
        idx += 1
    
    d0 = bfs(0, n - 1, g, n)
    d1 = bfs(1, n - 1, g, n)
    
    if d0 < d1:
        print(f"0 {d0}")
    elif d1 < d0:
        print(f"1 {d1}")
    else:
        print(f"0 {d0}")
