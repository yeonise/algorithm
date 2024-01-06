# 벨만-포드 알고리즘은 다익스트라 알고리즘의 한계점을 보완하기 위해 나왔다
# 음의 가중치를 갖는 사이클이 있는 경우 다익스트라 알고리즘은 무한히 비용이 작아지는 루프에 빠지게 된다
# 벨만-포드는 음의 사이클이 존재해도 최소 비용 경로를 계산할 수 있다.
# 다만 시간 복잡도가 증가하기 때문에 가중치가 모두 양수일 경우 다익스트라를 사용하는 것이 좋다
# Greedy한 다익스트라와 달리 벨만-포드 알고리즘은 모든 경우의 수를 고려하기 때문이다
# 다익스트라는 출발 노드에서 연결된 노드를 반복적으로 탐색하며 다른 모든 노드까지의 최소 거리를 구했다
# 반면 벨만-포드는 모든 노드가 한 번씩 출발점이 되어 다른 모든 노드까지의 최소 비용을 계산한다

def bellman_ford(start):  # O(VE)
    weights[start] = 0

    for i in range(vertex):
        for a, b, weight in graph:
            new_weight = weights[a] + weight

            if weights[a] != INF and weights[b] > new_weight:
                weights[b] = new_weight

                if i == vertex - 1:
                    return False  # there is negative cycle

    return True  # there is no cycle


vertex, edge = map(int, input().split())
graph = []
for _ in range(edge):
    graph.append([*map(int, input().split())])

INF = float('inf')
weights = [INF] * (vertex + 1)

if bellman_ford(1):  # 출발 노드를 매개변수로 설정한다
    print(weights)
else:
    print("There is negative cycle.")

'''
negative cycle
5 9
1 2 -6
1 3 3
1 4 9
1 5 8
2 3 -2
3 4 5
3 5 -7
4 3 -4
5 3 -13
'''

'''
[inf, 0, -6, -8, 9, 8]
5 7
1 2 -6
1 3 3
1 4 9
1 5 8
2 3 -2
4 3 -4
5 3 -13
'''
