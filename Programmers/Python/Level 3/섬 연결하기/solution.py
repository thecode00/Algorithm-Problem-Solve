# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    # 유니온 파인드로 연결되어있는 노드인지 판별
    parent = [n for n in range(n)]

    def find(num):
        if parent[num] != num:
            parent[num] = find(parent[num])
        return parent[num]

    def union(a, b):
        a, b = find(a), find(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    # 연결비용이 적은 순으로 정렬
    costs.sort(key=lambda x: x[2])

    answer = 0
    for a, b, cost in costs:
        # 연결되어있지 않은 노드 연결, 비용이 적은순으로 꺼내기때문에 이미 연결된 노드들은 고려할 필요가 없음
        if find(a) != find(b):
            answer += cost
            union(a, b)

    return answer
