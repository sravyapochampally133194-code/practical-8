def dfs(adj, src):
    v = len(adj)
    visited = [False] * v
    res = []
    stack = []

    stack.append(src)

    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = True
            res.append(curr)

            for i in reversed(adj[curr]):
                if not visited[i]:
                    stack.append(i)

    return res

graph = {
    0: [1, 5],
    1: [0, 2, 3, 4],
    2: [1],
    3: [1, 6],
    4: [1, 5],
    5: [0, 4],
    6: [3]
}

print("DFS Traversal starting from 0:")
print(dfs(graph, 0))


