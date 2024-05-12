asset = int(input())
stock = list(map(int, input().split()))

junhyeon = [asset, 0]
sungmin = [asset, 0]

continuity = 0

for i, s in enumerate(stock):
    # junhyeon
    junhyeon_can_buy = junhyeon[0] // s
    junhyeon[0] -= junhyeon_can_buy * s
    junhyeon[1] += junhyeon_can_buy

    # sungmin
    if 0 < i:
        if continuity >= 0 and s > stock[i - 1]:
            continuity += 1
        elif continuity <= 0 and s < stock[i - 1]:
            continuity -= 1
        else:
            if s > stock[i - 1]:
                continuity = 1
            elif s < stock[i - 1]:
                continuity = -1
            else:
                continuity = 0

    if continuity >= 3:
        sungmin[0] += s * sungmin[1]
        sungmin[1] = 0
    elif continuity <= -3:
        sungmin_can_buy = sungmin[0] // s
        sungmin[0] -= sungmin_can_buy * s
        sungmin[1] += sungmin_can_buy

junhyeon = junhyeon[0] + stock[-1] * junhyeon[1]
sungmin = sungmin[0] + stock[-1] * sungmin[1]

if junhyeon > sungmin:
    print("BNP")
elif junhyeon < sungmin:
    print("TIMING")
else:
    print("SAMESAME")
