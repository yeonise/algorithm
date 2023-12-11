# 로또

def combination(size, array):
    results = []

    def generate(index, temp):
        if len(temp) == size:
            results.append(temp[:])
            return

        for i in range(index, len(array)):
            temp.append(array[i])
            generate(i + 1, temp)
            temp.pop()

    generate(0, [])

    return results


numbers = [*map(int, input().split())]

while numbers[0] != 0:
    for group in combination(6, numbers[1:]):
        print(*group)

    numbers = [*map(int, input().split())]

    if numbers[0] != 0:
        print()
