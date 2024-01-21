from collections import defaultdict
from heapq import heappush, heappop


def solution(n, s, a, b, fares):
    # S에서 중간까지 가는 데 필요한 비용
    # +
    # 중간에서 B까지 가는 데 필요한 비용 + 중간에서 A까지 가는 데 필요한 비용

    graph = defaultdict(list)

    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    def find(start):
        from_start = [float('inf')] * (n + 1)
        from_start[start] = 0

        heap = []
        heappush(heap, (0, start))

        while heap:
            weight, current = heappop(heap)

            for node, w in graph[current]:
                updated_weight = weight + w

                if from_start[node] > updated_weight:
                    from_start[node] = updated_weight
                    heappush(heap, (updated_weight, node))

        return from_start

    from_start_cost = find(s)
    to_a_cost = find(a)
    to_b_cost = find(b)

    answer = float('inf')

    for mid in range(1, n + 1):
        answer = min(answer, from_start_cost[mid] + to_a_cost[mid] + to_b_cost[mid])

    return answer
