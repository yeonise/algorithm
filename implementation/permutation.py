def permutation(array, size):
    results = []
    used = [False] * len(array)

    def generate(temp):
        if len(temp) == size:
            results.append(temp[:])
            return

        for i in range(len(array)):
            if not used[i]:
                temp.append(array[i])
                used[i] = True
                generate(temp)
                used[i] = False
                temp.pop()

    generate([])

    return results


def permutation_with_repetition(array, size):
    results = []

    def generate(temp):
        if len(temp) == size:
            results.append(temp[:])
            return

        for i in range(len(array)):
            temp.append(array[i])
            generate(temp)
            temp.pop()

    generate([])

    return results
