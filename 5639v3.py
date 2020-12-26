import sys
sys.setrecursionlimit(10**9)

in_list = []


def postorder(start, end):
    length = end - start

    if length < 1:
        return

    elif length == 1:
        print(in_list[start])
        return

    root = in_list[start]

    idx = start+1
    while idx < end:
        if in_list[idx] > root:
            break

        idx += 1

    postorder(start+1, idx)
    postorder(idx, end)
    print(root)


for i in range(10000):
    try:
        n = int(sys.stdin.readline().strip())
        in_list.append(n)

    except:
        break

postorder(0, i)