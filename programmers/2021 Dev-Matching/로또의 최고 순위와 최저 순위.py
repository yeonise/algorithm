def solution(lottos, win_nums):
    result = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    hit = 0
    zero = 0

    for number in lottos:
        if number == 0:
            zero += 1
        elif number in win_nums:
            hit += 1

    return [result[hit + zero], result[hit]]
