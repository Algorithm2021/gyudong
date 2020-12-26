def dfs(graph, start):
    visited[start] = True

    for next in graph[start]:
        if not visited[next]:
            dfs(graph, next)


N = int(input())
pair = int(input())

connect = [set() for i in range(N)]
for i in range(pair):
    p1, p2 = map(int, input().split())

    connect[p1 - 1].add(p2 - 1)
    connect[p2 - 1].add(p1 - 1)

visited = [False for i in range(N)]
dfs(connect, 0)

print(sum(visited)-1)
