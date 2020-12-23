import sys
sys.setrecursionlimit(10**9)


def postorder(lst):
    if len(lst) == 0:
        return

    elif len(lst) == 1:
        print(lst[0])
        return

    root = lst.pop(0)

    idx = 0
    while idx < len(lst):
        if lst[idx] > root:
            break

        idx += 1

    left = lst[:idx]
    right = lst[idx:]

    postorder(left)
    postorder(right)
    print(root)


in_list = []
out_list = []


for i in range(10000):
    try:
        n = int(sys.stdin.readline().split()[0])
        in_list.append(n)

    except:
        break

postorder(in_list)
