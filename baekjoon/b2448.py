# 별 찍기 - 11

N = int(input())


def star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    stars = star(n // 2)
    results = []

    for s in stars:
        results.append(' ' * (n // 2) + s + ' ' * (n // 2))
    for s in stars:
        results.append(s + ' ' + s)

    return results


print('\n'.join(star(N)))
