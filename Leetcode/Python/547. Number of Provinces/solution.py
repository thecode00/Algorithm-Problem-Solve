# https://leetcode.com/problems/number-of-provinces/description/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = [False] * len(isConnected)

        def dfs(row: int):
            stack = [row]

            while stack:
                cur = stack.pop()

                for col in range(len(isConnected[cur])):
                    if isConnected[cur][col] == 1 and not visited[col]:
                        visited[col] = True
                        stack.append(col)

        for row in range(len(isConnected)):
            if not visited[row]:
                count += 1
                visited[row] = True
                dfs(row)

        return count
