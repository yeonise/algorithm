import sys

read = sys.stdin.readline
N, M = map(int, read().split())
trie = {'root': {}}

for _ in range(N):
    string = read().strip()
    current = trie['root']

    for char in string:
        if char not in current:
            current[char] = {}
        current = current[char]

    current['word'] = True

answer = 0

for _ in range(M):
    string = read().strip()
    current = trie['root']

    for char in string:
        if char in current:
            current = current[char]
        else:
            break
    else:
        if 'word' in current:
            answer += 1
        elif 'word' in current and len(current) >= 2:
            answer += 1
        elif 'word' not in current and len(current) >= 1:
            answer += 1

print(answer)
