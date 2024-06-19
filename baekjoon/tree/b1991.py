# 트리인가?
import sys

read = sys.stdin.readline

N = int(read())
tree = {}

for _ in range(N):
    node, left, right = read().split()
    tree[node] = (left, right)

preorder_result = []
inorder_result = []
postorder_result = []


def preorder(root):
    preorder_result.append(root)

    left, right = tree[root]

    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)


def inorder(root):
    left, right = tree[root]

    if left != '.':
        inorder(left)

    inorder_result.append(root)

    if right != '.':
        inorder(right)


def postorder(root):
    left, right = tree[root]

    if left != '.':
        postorder(left)

    if right != '.':
        postorder(right)

    postorder_result.append(root)


preorder('A')
inorder('A')
postorder('A')
print(''.join(preorder_result))
print(''.join(inorder_result))
print(''.join(postorder_result))
