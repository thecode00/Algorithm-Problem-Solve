# https://school.programmers.co.kr/learn/courses/30/lessons/92343


def solution(info, edges):
    visited = set()
    answer = []

    def dfs(sheep, wolves):
        if sheep > wolves:
            answer.append(sheep)
        else:
            return

        for parent, child in edges:
            # 부모노드는 방문가능했지만 늑대의 수 때문에 자식노드를 방문못한곳을 계속 탐색
            if parent in visited and child not in visited:
                visited.add(child)
                if info[child]:
                    dfs(sheep, wolves + 1)
                else:
                    dfs(sheep + 1, wolves)
                visited.remove(child)
    visited.add(0)
    dfs(1, 0)
    return max(answer)


# TEST
solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], 	[[0, 1], [1, 2], [1, 4], [
         0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
