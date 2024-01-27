import math


def solution(n, stations, w):
    stations.append(n + w + 1)
    previous = 1
    answer = 0

    for station in stations:
        distance = station - previous

        if distance > w:
            answer += math.ceil((station - w - previous) / (w * 2 + 1))

        previous = station + w + 1

    return answer
