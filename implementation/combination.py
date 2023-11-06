def combination(array, start, size):
    results = []

    def generate(index, temp):
        if len(temp) == size:
            results.append(temp[:])
            return

        if index >= len(array):
            return

        for i in range(index, len(array)):
            temp.append(array[i])
            generate(i + 1, temp)
            temp.pop()

    generate(start, [])

    return results


def combination_with_repetition(array, size):
    results = []

    def generate(index, temp):
        if len(temp) == size:
            results.append(temp[:])
            return

        if index >= len(array):
            return

        for i in range(index, len(array)):
            temp.append(array[i])
            generate(i, temp)
            temp.pop()

    generate(0, [])

    return results
