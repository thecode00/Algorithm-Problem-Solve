# https://leetcode.com/problems/task-scheduler/


from collections import Counter
import heapq

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
