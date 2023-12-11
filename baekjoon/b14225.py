# 부분 수열의 합 2
# 풀이 1

N = int(input())
numbers = [*map(int, input().split())]


def combination(array):
    number_sets = set(array)

    def generate(index, temp):
        if len(temp) > 0:
            number_sets.add(sum(temp))

        for i in range(index, len(array)):
            temp.append(array[i])
            generate(i + 1, temp)
            temp.pop()

    generate(0, [])

    return number_sets


number_sets = combination(numbers)

for i in range(1, 100000 * 20):
    if i not in number_sets:
        print(i)
        break

# 풀이 2

numbers.sort()

target = 0

for number in numbers:
    if target + 1 < number:
        break

    target += number

print(target + 1)
