from collections import deque

def bfs(adj, src):
    v = len(adj)
    visited = [False] * v
    res = []
    queue = deque()

    visited[src] = True
    queue.append(src)

    while queue:
        curr = queue.popleft()
        res.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

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

print("BFS Traversal starting from 0:")
print(bfs(graph, 0))
