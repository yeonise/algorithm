# 팰린드롬 만들기
from collections import Counter

name = input()

# 펠린드롬이 가능하려면 모두 짝수개 있던가 아니면 1개만 홀수 나머지는 짝수개 있어야 한다.

counter = Counter(list(name))
flag = False

for count in counter.values():
    if count % 2 != 0:
        if flag:
            print("I'm Sorry Hansoo")
            exit()
        else:
            flag = True

answer = ""
center = None

for alpha in sorted(counter.keys()):
    answer += alpha * (counter[alpha] // 2)

    if counter[alpha] % 2 != 0:
        center = alpha

if center:
    answer += center + answer[::-1]
else:
    answer += answer[::-1]

print(answer)
