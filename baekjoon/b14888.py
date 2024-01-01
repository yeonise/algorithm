# 연산자 끼워넣기

N = int(input())
numbers = [*map(int, input().split())]

# 순서 : + - * /
add, sub, mul, div = map(int, input().split())

max_result = -1e10
min_result = 1e10


def dfs(add, sub, mul, div, sum, idx):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return

    if add:
        dfs(add - 1, sub, mul, div, sum + numbers[idx], idx + 1)
    if sub:
        dfs(add, sub - 1, mul, div, sum - numbers[idx], idx + 1)
    if mul:
        dfs(add, sub, mul - 1, div, sum * numbers[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div - 1, int(sum / numbers[idx]), idx + 1)


dfs(add, sub, mul, div, numbers[0], 1)
print(max_result)
print(min_result)
