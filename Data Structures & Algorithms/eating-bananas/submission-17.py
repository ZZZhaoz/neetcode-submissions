class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r)//2
            if h < self.consume(mid, piles):
                l = mid + 1
            else:
                r = mid
        return l
       
       
    def consume(self, speed: int, piles: List[int]) -> int:
        res = 0
        for pile in piles:
            time = pile // speed
            if pile % speed == 0:
                res += time
            else:
                res += time + 1
        return res
    
       