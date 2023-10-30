import re
import collections


def solution(s):
    counter = collections.Counter(map(int, re.sub(r'[{}]', '', s).split(",")))

    return sorted([*counter.keys()], key=lambda x: (counter[x]), reverse=True)
