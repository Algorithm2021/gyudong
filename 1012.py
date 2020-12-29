from itertools import product
import sys

sys.setrecursionlimit(10**9)


def dfs(xp, yp):
    new_p = [[int(xp-1), int(xp+1)], [int(yp-1), int(yp+1)]]
    comb = list(product(*new_p))

    for point in comb:
        new_x, new_y = point

        if field[new_y][new_x]==1 and -1 < new_x < M and -1 < new_y < M:
            visited[new_y][new_x] = True
            dfs(new_x, new_y)


T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    worm = 0

    field = [[0 for m in range(M)] for n in range(N)]
    visited = [[False for m in range(M)] for n in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    for m, n in product(range(M), range(N)):
        if field[n][m]==1 and not visited[n][m]:
            worm += 1
            dfs(m, n)

    print(worm)