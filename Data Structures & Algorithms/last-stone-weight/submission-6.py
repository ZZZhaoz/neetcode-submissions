class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            
            if x < y:
                heapq.heappush(stones, -(y - x))
            
   
        if not stones:
            return 0
        else:
            return -stones[0]
        