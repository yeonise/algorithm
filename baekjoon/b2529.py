# 부등호

k = int(input())
relations = input().split()


def compare(array):
    for index, sign in enumerate(relations):
        if sign == '>':
            if array[index] <= array[index + 1]:
                return False
        else:
            if array[index] >= array[index + 1]:
                return False

    return True


def permutation(size, array):
    results = []
    used = [False] * len(array)

    def generate(temp):
        if len(temp) == size:
            if compare(temp):
                results.append(''.join(map(str, temp)))
            return

        for i in range(len(array)):
            if not used[i]:
                temp.append(array[i])
                used[i] = True
                generate(temp)

                if results:
                    return

                used[i] = False
                temp.pop()

    generate([])

    return results[0]


print(permutation(k + 1, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
print(permutation(k + 1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
