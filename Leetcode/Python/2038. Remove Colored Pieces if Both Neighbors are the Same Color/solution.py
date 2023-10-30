# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Count of times a block can be deleted.
        alice = bob = 0
        for idx in range(1, len(colors) - 1):
            if colors[idx - 1] == colors[idx] == colors[idx + 1]:
                if colors[idx] == "A":
                    alice += 1
                else:
                    bob += 1
        # If Alice and Bob are equal, Alice moves first, so return false.
        return alice > bob
