import collections


def solution(enroll, referral, seller, amount):
    tree = {}
    profits = collections.defaultdict(int)

    for i in range(len(enroll)):
        tree[enroll[i]] = referral[i]

    for i in range(len(seller)):
        person = seller[i]
        profit = amount[i] * 100

        while person != '-':
            pass_profit = int(profit * 0.1)
            real_profit = profit - pass_profit

            if real_profit >= 1:
                profits[person] += real_profit
            else:
                profits[person] += profit
                break

            profit = pass_profit
            person = tree[person]

    return [profits[p] for p in enroll]
