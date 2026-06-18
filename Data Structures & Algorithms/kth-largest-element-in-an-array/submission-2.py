class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [-s for s in nums]
        heapq.heapify(minheap)

        res = []
        while k > 0:
            e = heapq.heappop(minheap)
            res.append(-e)
            k -= 1

        return res[-1]

        
        
        