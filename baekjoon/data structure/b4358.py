# 생태학
from collections import defaultdict
import sys
read = sys.stdin.readline

dictionary = defaultdict(int)
total = 0

while True:
    tree = read().strip()

    if not tree:
        break

    dictionary[tree] += 1
    total += 1

names = list(dictionary.keys())
names.sort()

for name in names:
    print(name, format(dictionary[name] / total * 100, ".4f"))
