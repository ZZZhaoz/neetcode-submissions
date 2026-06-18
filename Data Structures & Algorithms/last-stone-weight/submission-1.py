class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-x for x in stones]
        heapq.heapify(s)
        while len(s) > 1:
            first = heapq.heappop(s)
            second = heapq.heappop(s)
            if first == second:
                pass
            
            else:
                heapq.heappush(s, first - second)

        if not s:
            return 0
        return -s[0]
        