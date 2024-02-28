from collections import defaultdict


def solution(want, number, discount):
    answer = 0

    wishlist = {want[i]: number[i] for i in range(len(want))}
    count = sum(number)

    for i in range(10):
        product = discount[i]

        if product in wishlist:
            count -= wishlist[product] > 0
            wishlist[product] -= 1

    if count == 0:
        answer += 1

    index = 10

    while len(discount) > index:
        out = discount[index - 10]
        new = discount[index]

        if out in wishlist:
            count += wishlist[out] >= 0
            wishlist[out] += 1

        if new in wishlist:
            count -= wishlist[new] > 0
            wishlist[new] -= 1

        if count == 0:
            answer += 1

        index += 1

    return answer
