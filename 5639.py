import sys
sys.setrecursionlimit(10**9)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_left(self, value):
        self.left = Node(value)

    def set_right(self, value):
        self.right = Node(value)


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        temp = self.root

        while True:
            if value < temp.value:
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.set_left(value)
                    break

            elif value > temp.value:
                if temp.right is not None:
                    temp = temp.right
                else:
                    temp.set_right(value)
                    break


result = []


def postorder(temp_node):
    if temp_node.left is not None:
        postorder(temp_node.left)

    if temp_node.right is not None:
        postorder(temp_node.right)

    return result.append(temp_node.value)


binary_tree = BinaryTree(int(sys.stdin.readline().split()[0]))

for i in range(9999):
    try:
        n = int(sys.stdin.readline().split()[0])
        binary_tree.insert(n)

    except:
        break

postorder(binary_tree.root)

for num in result:
    print(num)