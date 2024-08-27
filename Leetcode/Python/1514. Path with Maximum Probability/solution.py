# https://leetcode.com/problems/path-with-maximum-probability/description/
# Time complexity: O((N + E) log N), N = number of node, E = number of edge


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        probability = [0] * n
        probability[start] = 1
        graph = [[] for _ in range(n)]

        for idx in range(len(edges)):
            n1, n2 = edges[idx]
            weight = succProb[idx]
            graph[n1].append((weight, n2))
            graph[n2].append((weight, n1))

        heap = []
        heapq.heappush(heap, (-1.0, start))  # For max_heap change to negative
        while heap:
            cur_prob, cur_node = heapq.heappop(heap)
            cur_prob *= -1
            if cur_prob < probability[cur_node]:
                continue

            for prob, node in graph[cur_node]:
                temp_prob = cur_prob * prob
                if temp_prob > probability[node]:
                    probability[node] = temp_prob
                    heapq.heappush(heap, (-temp_prob, node))

        return probability[end]


class Solution:  # BFS
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Make Adjacency list
        adj_list = [[] for _ in range(n)]

        for edge, prob in list(zip(edges, succProb)):
            a, b = edge
            adj_list[a].append((b, prob))
            adj_list[b].append((a, prob))

        probs = [-float("inf")] * n
        probs[start_node] = 1
        queue = deque()
        queue.append(start_node)

        while queue:
            cur = queue.popleft()

            for next, p in adj_list[cur]:
                new_prob = probs[cur] * p
                if probs[next] < new_prob:
                    queue.append(next)
                    probs[next] = new_prob

        return probs[end_node] if probs[end_node] > 0 else 0
