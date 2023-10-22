# https://leetcode.com/problems/n-queens/description/


from typing import List, Dict, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def find_queen(queen: int, diag1: Set, diag2: Set, cols: Dict) -> None:
            if queen == n:  # Found queens potision
                result.append(list(cols.keys()))
                return
            for x in range(n):
                # cols = Queen's column index, diag1 = \ diagonal, diag2 = / diagonal
                if x in cols or queen + x in diag1 or queen - x in diag2:
                    continue
                cols[x] = 1
                diag1.add(queen + x)
                diag2.add(queen - x)
                find_queen(queen + 1, diag1, diag2, cols)
                del cols[x]
                diag1.remove(queen + x)
                diag2.remove(queen - x)

        find_queen(0, set(), set(), dict())

        for board in result:  # Draw board
            for idx in range(len(board)):
                pos = board[idx]
                board[idx] = "." * pos + "Q" + "." * (len(board) - pos - 1)

        return result


a = Solution()
print(a.solveNQueens(1))
