def solution(edges):
    graph = {}

    for a, b in edges:
        if a not in graph:
            graph[a] = [0, 0]  # [in, out]
        if b not in graph:
            graph[b] = [0, 0]  # [in, out]

        graph[a][1] += 1
        graph[b][0] += 1

    # 각 그래프의 개수 세기
    # 아무도 방문하지 않으면서 2번 이상 밖으로 나가는 정점이 새로 생성한 정점이다
    # 1번 방문하면서 밖으로 나가지 않는 정점의 개수가 막대 모양 그래프의 개수이다
    # 2번 이상 방문하면서 2번 이상 밖으로 나가는 정점의 개수가 8자 모양 그래프의 개수이다
    # 새로 생성한 정점에서 밖으로 나가는 간선의 수 - 막대 모양 그래프의 수 - 8자 모양 그래프의 수 = 도넛 모양 그래프의 수
    point = 0
    donut = 0
    stick = 0
    eight = 0

    for key, counter in graph.items():
        in_count = counter[0]
        out_count = counter[1]

        if out_count >= 2 and in_count == 0:  # if point
            point = key
        elif out_count == 0 and in_count > 0:  # if stick
            stick += 1
        elif out_count >= 2 and in_count >= 2:  # if eight
            eight += 1

    donut = graph[point][1] - stick - eight

    return [point, donut, stick, eight]
