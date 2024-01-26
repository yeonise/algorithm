def solution(n, s):
    if s // n == 0:
        return [-1]

    piece = s // n
    rest = s % n
    answer = [piece] * n

    if rest == 0:
        return answer

    plus = rest // n
    last = rest % n

    if plus > 0:
        answer = [a + plus for a in answer]
    if last > 0:
        for i in range(last):
            answer[n - 1 - i] += 1

    return answer
