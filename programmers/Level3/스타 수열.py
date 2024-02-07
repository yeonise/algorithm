from collections import Counter


def solution(a):
    if len(a) < 2:
        return 0

    if len(a) == 2:
        return 2

    counter = Counter(a)
    used = sorted(counter.items(), key=lambda x: -x[1])
    max_couple = 0

    for number, count in used:

        if count > max_couple:

            couple_count = 0
            index = 1

            while index < len(a):
                if a[index - 1] != a[index] and (a[index - 1] == number or a[index] == number):
                    couple_count += 1
                    index += 2
                else:
                    index += 1

            max_couple = max(max_couple, couple_count)

        else:
            break

    return max_couple * 2
