import collections

sound = input()

if len(sound) % 5 != 0:
    print(-1)
    exit()

stack = []
count = collections.defaultdict(int)
order = {'q': [], 'u': [], 'a': [], 'c': [], 'k': []}

for index, char in enumerate(sound):
    order[char].append(index)

    if char == 'q':
        stack.append('q')
    elif char == 'k':
        if not stack:
            stack.append('k')
            break

        if stack[-1] == 'q':
            count[len(stack)] += 1
            stack.pop()
        else:
            stack.append('k')

if stack:
    print(-1)
    exit()

for value in order.values():
    if len(value) != len(sound) // 5:
        print(-1)
        exit()

for _ in range(len(sound) // 5):
    k = order['k'].pop()
    c = order['c'].pop()
    a = order['a'].pop()
    u = order['u'].pop()
    q = order['q'].pop()

    if not k > c > a > u > q:
        print(-1)
        exit()

print(len(count.keys()))
