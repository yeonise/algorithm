def solution(gems):
    counter = {}

    for gem in gems:
        counter[gem] = 1

    kind = len(counter)
    left = start = end = 0
    answer = []

    for right, gem in enumerate(gems, 1):
        kind -= counter[gem] > 0
        counter[gem] -= 1

        if kind == 0:
            while counter[gems[left]] < 0:
                counter[gems[left]] += 1
                left += 1

            if not end or right - left < end - start:
                start, end = left, right
                answer = [start + 1, end]

            counter[gems[left]] += 1
            left += 1
            kind += 1

    return answer
