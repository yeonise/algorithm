def solution(n, money):
    # 해당 금액을 거슬러 줄 수 있는 경우의 수를 모두 구해서 곱하기
    case = [1] + [0] * n  # [1, 0, 0, 0]
    money.sort()

    for coin in money:  # coin : 1, 2, 5
        for price in range(coin, n + 1):  # price : [1, 2, 3, 4, 5], [2, 3, 4, 5], [5]
            # 현재 price를 지불할 수 있는 경우의 수 += price - coin을 지불할 수 있는 경우의 수 + price
            case[price] += case[price - coin]  # case[price] : case[1 - 1], case[2 - 1], case[3 - 1], ...

    return case[-1] % 1_000_000_007
