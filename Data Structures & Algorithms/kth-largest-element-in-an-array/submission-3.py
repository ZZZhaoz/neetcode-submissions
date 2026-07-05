class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ns = [-num for num in nums]
        heapq.heapify(ns)
        i = 0
        while i < k:
            a = heapq.heappop(ns)
            i += 1
        return -a