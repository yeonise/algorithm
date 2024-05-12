import collections
import sys

input = sys.stdin.readline

N = int(input())
dictionary = collections.defaultdict(int)

for _ in range(N):
    _, extension = input().rstrip().split(".")
    dictionary[extension] += 1


keys = list(dictionary.keys())
keys.sort()

for key in keys:
    print(key, dictionary[key])
