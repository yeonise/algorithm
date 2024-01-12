# 별 찍기 - 10

N = int(input())


def star(n):
    if n == 3:
        return ['***', '* *', '***']

    stars = star(n // 3)
    results = []

    for s in stars:
        results.append(s * 3)
    for s in stars:
        results.append(s + ' ' * (n // 3) + s)
    for s in stars:
        results.append(s * 3)

    return results


print('\n'.join(star(N)))
