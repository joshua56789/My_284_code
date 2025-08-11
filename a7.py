from builtins import int, len, list, map, print, range, sorted, str
import sys

def DFS(G):
    S = []
    n = len(G)
    colour = ['WHITE'] * n
    pred = [None] * n
    seen = [0] * n
    done = [0] * n
    time = [0]
    
    for u in range(n):
        colour[u] = 'WHITE'
        pred[u] = None

    for v in range(n):
        if colour[v] == 'WHITE':
            DFSVisit(v, G, S, colour, pred, seen, done, time)

    return pred, seen, done

def DFSVisit(s, G, S, colour, pred, seen, done, time):
    colour[s] = 'GREY'
    seen[s] = time[0]
    time[0] += 1
    S.append(s)

    while S:
        u = S[-1]
        found_white = False
        for v in sorted(G[u]):
            if colour[v] == 'WHITE':
                colour[v] = 'GREY'
                pred[v] = u
                seen[v] = time[0]
                time[0] += 1
                S.append(v)
                found_white = True
                break

        if not found_white:
            S.pop()
            colour[u] = 'BLACK'
            done[u] = time[0]
            time[0] += 1

def longest_path(u, G, pred, longest_path_dp):
    if longest_path_dp[u] != -1:
        return longest_path_dp[u]
    max_length = 0
    for v in G[u]:
        if pred[v] == u:
            max_length = max(max_length, 1 + longest_path(v, G, pred, longest_path_dp))
    longest_path_dp[u] = max_length
    return max_length

def classify_edges_and_longest_path(G, pred, seen, done):
    tree_arcs = 0
    forward_arcs = 0
    back_arcs = 0
    cross_arcs = 0
    n = len(G)
    longest_path_dp = [-1] * n
    longest_path_length = 0

    for u in range(n):
        for v in G[u]:
            if pred[v] == u:
                tree_arcs += 1
            elif seen[u] < seen[v] and done[u] > done[v]:
                forward_arcs += 1
            elif seen[u] > seen[v] and done[u] < done[v]:
                back_arcs += 1
            elif done[u] < seen[v] or seen[u] > done[v]:
                cross_arcs += 1

    for u in range(n):
        if pred[u] is None:
            longest_path_length = max(longest_path_length, longest_path(u, G, pred, longest_path_dp))
    
    return tree_arcs, forward_arcs, back_arcs, cross_arcs, longest_path_length

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

for idx, (n, adj) in enumerate(dgs):
    pred, seen, done = DFS(adj)
    tree_arcs, forward_arcs, back_arcs, cross_arcs, longest_path_length = classify_edges_and_longest_path(adj, pred, seen, done)
    print(" ".join(map(str, [tree_arcs, forward_arcs, back_arcs, cross_arcs, longest_path_length])))

