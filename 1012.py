import sys

sys.setrecursionlimit(10**5)


def dfs(xp, yp):
    field[yp][xp] = 0

    if xp-1>=0 and field[yp][xp-1]!=0:
        dfs(xp-1, yp)

    if xp+1<M and field[yp][xp+1]!=0:
        dfs(xp+1, yp)

    if yp-1>=0 and field[yp-1][xp]!=0:
        dfs(xp, yp-1)

    if yp+1<N and field[yp+1][xp]!=0:
        dfs(xp, yp+1)


T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    worm = 0

    field = [[0 for m in range(M)] for n in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    for p in range(M*N):
        y = p//M
        x = p - y*M

        if field[y][x]==1:
            worm += 1
            dfs(x, y)

    print(worm)
