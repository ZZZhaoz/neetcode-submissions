class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = [-x for x in nums]
        heapq.heapify(s)
        i = 0
        while i < k:
            a = heapq.heappop(s)
            i += 1
        return -a
        
        
        