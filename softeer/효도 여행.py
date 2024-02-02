import sys
from collections import defaultdict
from collections import deque

vertex_count, string_length = map(int, sys.stdin.readline().split())
walking_path = sys.stdin.readline().strip()

graph = defaultdict(list)

for _ in range(vertex_count - 1):
    node1, node2, char = sys.stdin.readline().split()
    node1, node2 = int(node1), int(node2)
    graph[node1].append((node2, char))
    graph[node2].append((node1, char))

visited = [False] * (vertex_count + 1)
visited[1] = True
queue = deque([(1, '')])
strings = []

while queue:
    current, char = queue.popleft()

    count = 0
    for child in graph[current]:
        if not visited[child[0]]:
            visited[child[0]] = True
            queue.append((child[0], char + child[1]))
            count += 1

    if count == 0:
        strings.append(char)

strings.sort(key=len, reverse=True)
max_happiness = 0

for s in strings:
    if len(s) <= max_happiness:
        break

    if len(s) == len(walking_path) and s == walking_path:
        print(len(s))
        exit()

    dp = [[0] * (len(walking_path) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(walking_path) + 1):
            if s[i - 1] == walking_path[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    max_happiness = max(max_happiness, dp[-1][-1])

print(max_happiness)

# 1		정답	0.106 초	36.00 MB
# 2		정답	0.097 초	37.00 MB
# 3		정답	0.113 초	37.00 MB
# 4		오답	2.095 초	428.00 MB (미해결)
# 5		정답	0.130 초	39.00 MB
# 6		정답	0.135 초	46.00 MB
# 7		정답	0.147 초	39.00 MB
# 8		정답	0.198 초	62.00 MB
# 9		정답	0.137 초	39.00 MB
# 10	정답	0.296 초	94.00 MB
# 11	정답	0.135 초	40.00 MB
# 12	정답	0.381 초	124.00 MB
# 13	정답	0.344 초	42.00 MB
# 14	정답	0.171 초	53.00 MB
# 15	정답	0.159 초	45.00 MB
# 16	정답	0.408 초	130.00 MB
# 17	정답	0.137 초	38.00 MB
# 18	정답	0.557 초	179.00 MB
# 19	정답	0.146 초	43.00 MB
# 20	정답	0.704 초	230.00 MB
