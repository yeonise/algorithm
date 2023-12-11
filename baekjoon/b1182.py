# 부분 수열의 합

N, S = map(int, input().split())


def combination(array, target):
    results = [0]

    def generate(index, temp):
        if len(temp) > len(array):
            return

        if len(temp) > 0 and sum(temp) == target:
            results[0] += 1

        for i in range(index, len(array)):
            temp.append(array[i])
            generate(i + 1, temp)
            temp.pop()

    generate(0, [])

    return results[0]


numbers = [*map(int, input().split())]

print(combination(numbers, S))
