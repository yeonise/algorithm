# 단어 수학
from collections import defaultdict

N = int(input())
words = []
points = defaultdict(int)

for _ in range(N):
    word = input()
    words.append(word)

    for index, char in enumerate(word):
        points[char] += 10 ** (len(word) - index)

result = sorted(list(points.items()), key=lambda x: -x[1])

numbers = {}

for index, item in enumerate(result):
    numbers[item[0]] = str(9 - index)

answer = []

for word in words:
    number = ''
    for char in word:
        number += numbers[char]

    answer.append(int(number))

print(sum(answer))
