# https://leetcode.com/problems/kth-largest-element-in-an-array/


import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            # Change n to negative to make the heap max_heap.
            heapq.heappush(heap, -n)

        for _ in range(k - 1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)  # heapify convert list to heap

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlargest() automatically uses heapify()
        return heapq.nlargest(nums, k)


class Solution:  # Use sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
