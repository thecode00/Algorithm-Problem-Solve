# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_recolor = 0

        # First k block
        for idx in range(k):
            if blocks[idx] == "W":
                current_recolor += 1

        min_recolor = min(min_recolor, current_recolor)

        for idx in range(k, len(blocks)):
            if blocks[idx] == "W":
                current_recolor += 1
            if blocks[idx - k] == "W":
                current_recolor -= 1

            min_recolor = min(min_recolor, current_recolor)

        return min_recolor
