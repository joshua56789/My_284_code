from collections import defaultdict
import sys

# Calculate max tree profit
def maxProfitTree(nodes, edges):
    tree = defaultdict(list)
    
    for i in range(nodes - 1):
        parent, weight = edges[2 * i], edges[2 * i + 1]
        tree[parent].append((i + 1, weight))
    
    def dfs(node):
        if node not in tree:
            return 0, 0
        
        maxSingleBranch = 0
        maxCombined = 0
        topTwoBranches = [0, 0]

        for child, weight in tree[node]:
            childSingleBranch, childCombined = dfs(child)
            childProfit = childSingleBranch + weight

            if childProfit > topTwoBranches[0]:
                topTwoBranches = [childProfit, topTwoBranches[0]]
            elif childProfit > topTwoBranches[1]:
                topTwoBranches[1] = childProfit

            maxCombined = max(maxCombined, childCombined)
        
        combinedProfit = topTwoBranches[0] + topTwoBranches[1]
        maxCombined = max(maxCombined, combinedProfit)

        return topTwoBranches[0], maxCombined

    maxSingle, maxCombined = dfs(0)

    return max(0, maxSingle, maxCombined)


data = sys.stdin.read().strip().splitlines()
index = 0
results = []

while index < len(data):
    line = data[index].strip()

    nodes = int(line)
    index += 1
        
    if nodes == 0:
        break
        
    edgeLine = data[index].strip()
    edges = list(map(int, edgeLine.split()))
    index += 1

    result = maxProfitTree(nodes, edges)
    results.append(result)
    
for result in results:
    print(result)
