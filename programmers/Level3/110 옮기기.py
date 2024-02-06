def move(code):
    length = len(code)
    temp = []
    count = 0

    for number in code:
        temp.append(number)

        if len(temp) >= 3:
            if temp[-3:] == ['1', '1', '0']:
                count += 1
                temp.pop()
                temp.pop()
                temp.pop()

    result = ''
    last_zero = -1

    for index, number in enumerate(temp):
        result += number
        if number == '0':
            last_zero = index

        if len(result) >= 2:
            if result[-2:] == '11':
                result = result[:-2] + '110' * count + ''.join(temp[index + 1:])
                break

    if len(result) == length:
        return result

    if last_zero == -1:
        return '110' * count + ''.join(temp)
    else:
        return ''.join(temp[:last_zero + 1]) + '110' * count + ''.join(temp[last_zero + 1:])


def solution(s):
    return [move(code) for code in s]
