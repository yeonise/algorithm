# 배열 합치기
import sys

read = sys.stdin.readline
a_size, b_size = map(int, read().split())
a_list = list(map(int, read().split()))
b_list = list(map(int, read().split()))
a_pointer = b_pointer = 0
result = []

while a_pointer < a_size and b_pointer < b_size:
    if a_list[a_pointer] < b_list[b_pointer]:
        result.append(a_list[a_pointer])
        a_pointer += 1
    elif a_list[a_pointer] > b_list[b_pointer]:
        result.append(b_list[b_pointer])
        b_pointer += 1
    else:
        result.append(a_list[a_pointer])
        result.append(b_list[b_pointer])
        a_pointer += 1
        b_pointer += 1

while a_pointer < a_size:
    result.append(a_list[a_pointer])
    a_pointer += 1

while b_pointer < b_size:
    result.append(b_list[b_pointer])
    b_pointer += 1

print(*result)
