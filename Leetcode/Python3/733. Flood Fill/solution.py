# https://leetcode.com/problems/flood-fill/

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


class Solution:  # Runtime: 140ms
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:    # If starting pixel is already same color no need to change
            return image
        q = []
        q.append((sr, sc))
        image[sr][sc] = color
        while q:    # change color using dfs
            y, x = q.pop()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny and ny < len(image) and 0 <= nx and nx < len(image[0]) and image[ny][nx] == start_color:
                    q.append((ny, nx))
                    image[ny][nx] = color
        return image
