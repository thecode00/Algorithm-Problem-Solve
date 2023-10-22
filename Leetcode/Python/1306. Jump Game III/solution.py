# https://leetcode.com/problems/jump-game-iii/


from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)
        visited = set([start])  # Prevent redundant search
        q = deque([start])
        while q:    # BFS
            idx = q.popleft()
            if arr[idx] == 0:
                return True
            if 0 <= idx + arr[idx] < length and idx + arr[idx] not in visited:
                q.append(idx + arr[idx])
                visited.add(idx + arr[idx])
            if 0 <= idx - arr[idx] and idx - arr[idx] not in visited:
                q.append(idx - arr[idx])
                visited.add(idx - arr[idx])
        return False
            