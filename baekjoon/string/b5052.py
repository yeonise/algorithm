# 전화번호 목록
class Node:
    def __init__(self, val):
        self.val = val
        self.flag = False
        self.children = {}


import sys

read = sys.stdin.readline

t = int(read())

for _ in range(t):
    n = int(read())
    numbers = sorted([read().strip() for _ in range(n)])
    trie = {'root': {}}
    flag = False

    for number in numbers:
        current = trie['root']

        for char in number:
            if 'N' in current:
                flag = True
                break

            if char not in current:
                current[char] = {}

            current = current[char]
        else:
            current['N'] = True

        if flag:
            break

    if flag:
        print('NO')
    else:
        print('YES')
