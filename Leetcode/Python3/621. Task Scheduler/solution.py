# https://leetcode.com/problems/task-scheduler/


from collections import Counter
import heapq
from typing import List

# TODO: 다른방법으로 풀기


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        count = Counter(tasks)
        while count:
            sub_count = 0
            for t, _ in count.most_common(n + 1):
                count.subtract(t)
                print(count, t)
                # Add an empty counter to remove elements below zero.
                count += Counter()
                result += 1
                sub_count += 1

            result += n - sub_count + 1

        return 0


# Ref: https://leetcode.com/problems/task-scheduler/solutions/104504/c-8lines-o-n/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        count = Counter(tasks)
        most = count.most_common(1)[0][1]
        # Except last task of most task
        # Why (n + 1)? ex. tasks = ["A", "A"], n = 2 -> "A" - IDLE - IDLE - "A"
        # Include cooldown time(n) and complete task time(1)
        result = (most - 1) * (n + 1)
        
        for val in count.values():
            # Now add last task of most task
            if val == most:
                result += 1;
        # Ex. tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], n = 2
        # A##A##A -> AB#AB#AB -> ABCABCABC -> ABC(D)ABC(D)ABC -> ABCD(E)ABCDABC
        # We can insert every task end of most task cycle(ABC)
        return max(result, len(tasks))

