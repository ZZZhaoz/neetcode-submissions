class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new = []
        for x in nums:
            new.append(-x)
        heapq.heapify(new)
        
        i = 0
        while i < k - 1:
            heapq.heappop(new)

            i += 1
        res = heapq.heappop(new)
        return -res
        
        