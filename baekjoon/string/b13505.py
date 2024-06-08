# 두 수 XOR
N = int(input())
numbers = list(map(int, input().split()))
length = len(bin(max(numbers))[2:])
trie = {'root': {}}

for number in numbers:
    bin_number = bin(number)[2:].zfill(length)
    current = trie['root']

    for digit in bin_number:
        if digit not in current:
            current[digit] = {}

        current = current[digit]

answer = 0

for number in numbers:
    bin_number = bin(number)[2:].zfill(length)
    current = trie['root']
    other_number = ''

    for digit in bin_number:
        reverse = '0' if digit == '1' else '1'

        if reverse in current:
            other_number += reverse
            current = current[reverse]
        else:
            other_number += digit
            current = current[digit]

    answer = max(answer, number ^ int(other_number, 2))

print(answer)
