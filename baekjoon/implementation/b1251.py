# 단어 나누기
word = input()

# 시작 지점 3개를 선택한다
# ex. 1, 2, 3 / 1, 2, 4 / ...
# 첫 시작 지점은 무조건 1일 수 밖에 없다
results = []

for second in range(1, len(word) - 1):
    for third in range(second + 1, len(word)):
        one = word[:second][::-1]
        two = word[second:third][::-1]
        three = word[third:][::-1]

        results.append(one + two + three)

results.sort()

print(results[0])
