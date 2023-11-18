def solution(survey, choices):
    score = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0}
    pair = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    point = {
        1: 3, 2: 2, 3: 1,
        5: 1, 6: 2, 7: 3}

    for index, choice in enumerate(choices):
        if choice >= 5:
            score[survey[index][1]] += point[choice]
        elif choice == 4:
            continue
        else:
            score[survey[index][0]] += point[choice]

    mbti = ""

    for t1, t2 in pair:
        if score[t1] < score[t2]:
            mbti += t2
        else:
            mbti += t1

    return mbti
