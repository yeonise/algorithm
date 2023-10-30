from itertools import permutations


def solution(user_id, banned_id):
    passed_group = set()

    for group in permutations(user_id, len(banned_id)):

        count = 0

        for index, user in enumerate(group):
            if len(user) == len(banned_id[index]):
                match = 0
                for char_index, char in enumerate(banned_id[index]):
                    if char == '*' or user[char_index] == char:
                        match += 1
                    else:
                        break
                if match == len(user):
                    count += 1
            else:
                break

        if count == len(banned_id):
            passed_group.add(tuple(sorted(list(group))))

    return len(passed_group)
