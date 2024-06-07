# 고냥이
from collections import defaultdict

N = int(input())
strings = input()
counter = defaultdict(int)
strings_set = set()

max_length = 0
left = 0
right = 1
counter[strings[left]] += 1
strings_set.add(strings[left])

while right < len(strings):
    counter[strings[right]] += 1
    strings_set.add(strings[right])

    if len(strings_set) > N:
        while len(strings_set) > N:
            counter[strings[left]] -= 1

            if counter[strings[left]] == 0:
                strings_set.remove(strings[left])

            left += 1

    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)
