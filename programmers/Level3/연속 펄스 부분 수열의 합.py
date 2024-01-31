def solution(sequence):
    pulse1 = []  # [1, -1, 1, -1, ...]
    pulse2 = []  # [-1, 1, -1, 1, ...]

    for i, number in enumerate(sequence):
        if i % 2 == 0:
            pulse1.append(number)
            pulse2.append(-number)
        else:
            pulse1.append(-number)
            pulse2.append(number)

    dp1 = [0] * len(sequence)
    dp2 = [0] * len(sequence)
    dp1[0] = pulse1[0]
    dp2[0] = pulse2[0]
    answer = max(dp1[0], dp2[0])

    for i in range(1, len(sequence)):
        dp1[i] = max(pulse1[i], dp1[i - 1] + pulse1[i])
        dp2[i] = max(pulse2[i], dp2[i - 1] + pulse2[i])

        answer = max(answer, dp1[i], dp2[i])

    return answer
