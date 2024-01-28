def solution(scores):
    whanho = scores[0]
    whanho_score = sum(whanho)

    candidates = []
    for i in range(len(scores)):
        if sum(scores[i]) > whanho_score:
            candidates.append(scores[i])

    if not candidates:
        return 1

    candidates.sort(key=lambda x: (-x[0], x[1]))
    rank = 1
    a_standard = candidates[0][0]
    b_standard = candidates[0][1]
    for sa, sb in candidates:
        if a_standard <= sa or b_standard <= sb:
            rank += 1

        b_standard = max(b_standard, sb)

        if whanho[0] < sa and whanho[1] < sb:
            return -1

    return rank
