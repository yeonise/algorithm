# 하나의 출발점에서 다른 모든 노드들까지의 최단 거리를 구하는 다익스트라 알고리즘, 벨만-포드 알고리즘과 다르게
# 플로이드-와샬 알고리즘은 모든 노드 간의 최단 거리를 구할 수 있다
# 플로이드-와샬 알고리즘은 음의 가중치가 있어도 최단 거리를 구할 수 있으나, 음의 사이클이 존재한다면 사용할 수 없다
# 음의 사이클이 존재한다면 벨만-포드 알고리즘을 사용해야 한다
# 다익스트라가 1차원 배열을 사용한다면, 플로이드-와샬 알고리즘은 2차원 배열을 사용하여 memorize한다
# 플로이드-와샬 알고리즘의 핵심은 각 단계마다 특정한 노드 k를 거쳐 가는 경우를 확인하는 것이다
# 점화식 : D[i][j] = min(D[i][i], D[i][k] + D[k][j])
# i에서 j로 가는 것과 i에서 k를 거쳐 j로 가는 것 중 어느 것이 최소 비용인지 계산한다
# 3중 반복문을 사용하여 구현한다

def floyd_warshall():  # O(n^3)
    for k in range(1, vertex + 1):  # via
        graph[k][k] = 0  # 사이클이 없으므로 자신을 향하는 가중치를 0으로 초기화한다

        for i in range(1, vertex + 1):
            for j in range(1, vertex + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


vertex, edge = map(int, input().split())
INF = float('inf')
graph = [[INF] * (vertex + 1) for _ in range(vertex + 1)]

for _ in range(edge):
    a, b, weight = map(int, input().split())
    graph[a][b] = weight

floyd_warshall()

for i in range(1, vertex + 1):
    for j in range(1, vertex + 1):
        print(graph[i][j], end=' ')
    print()

'''
4 7
1 2 5
1 4 7
2 1 4
2 3 -3
3 1 6
3 4 4
4 3 2
'''

# 0 5 2 6
# 3 0 -3 1
# 6 11 0 4
# 8 13 2 0
