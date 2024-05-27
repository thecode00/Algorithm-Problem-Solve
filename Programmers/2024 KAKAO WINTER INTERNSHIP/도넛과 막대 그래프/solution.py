# https://school.programmers.co.kr/learn/courses/30/lessons/258711?language=python3

def solution(edges):
    # [노드의 진입차수, 노드의 진출차수]
    node_info = {}

    for a, b in edges:
        if a not in node_info:
            node_info[a] = [0, 0]
        if b not in node_info:
            node_info[b] = [0, 0]

        node_info[a][1] += 1
        node_info[b][0] += 1

    answer = [0, 0, 0, 0]
    total_graph = 0

    # 진입 노드와 그래프들의 종류 판별
    for node in node_info.keys():
        indegree, outdegree = node_info[node]
        if indegree == 0 and outdegree >= 2:
            answer[0] = node
            # 전체 그래프 개수는 진입 노드에 연결되어있는 노드 개수
            total_graph = outdegree
        elif indegree >= 1 and outdegree == 0:  # 막대 그래프 정점수로 막대 그래프 개수 세기
            answer[2] += 1
        elif indegree >= 1 and outdegree >= 2:  # 8자 그래프의 중심 노드로 8자 그래프 개수 세기
            answer[3] += 1

    answer[1] = total_graph - answer[2] - answer[3]
    return answer
