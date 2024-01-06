import heapq


def dijkstra(start):  # O((V+E) log V)
    heap = []
    heapq.heappush(heap, (0, start))  # 첫 번째 값을 기준으로 정렬된다
    INF = float('inf')  # Infinite
    weights = [INF] * (vertex + 1)  # DP에 활용할 memorization 테이블을 생성한다
    weights[start] = 0  # 자기 자신으로 향하는 경우의 최소 비용 설정

    while heap:
        weight, node = heapq.heappop(heap)
        print(node, weight)

        if weight > weights[node]:  # 현재의 최소 비용보다 크다면 넘어간다
            continue

        for n, w in graph[node]:  # 최소 비용을 가진 노드를 방문한 경우 연결된 간선을 모두 확인한다
            new_weight = weight + w

            if weights[n] > new_weight:  # 새로운 가중치가 더 작다면
                weights[n] = new_weight  # 최소 가중치 갱신
                heapq.heappush(heap, (new_weight, n))  # 최소 비용을 갖는 노드를 힙에 추가

    return weights


vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]

for i in range(edge):
    a, b, weight = map(int, input().split())
    graph[a].append([b, weight])

answer = dijkstra(start)
print(answer)  # [inf, 0, 3, 5, 6, 8]

'''
5 6 1
1 2 3
2 3 2
3 4 1
3 5 3
1 4 8
1 5 9
'''
