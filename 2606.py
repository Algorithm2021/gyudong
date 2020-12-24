def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


N = int(input())
pair = int(input())

connect = ['' for i in range(N)]
for i in range(pair):
    p1, p2 = map(int, input().split())

    connect[p1 - 1] += str(p2 - 1)
    connect[p2 - 1] += str(p1 - 1)

unique_connect = {}
for i in range(N):
    unique_connect[str(i)] = set(connect[i])

result = dfs(unique_connect, '0')
print(result)

print(len(result)-1)
