class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = (l + r)//2
            if self.consume(piles, mid) <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    
    def consume(self, piles: List[int], k: int):
        count = 0
        for pile in piles:
            count = count + (pile // k)
            if pile % k > 0:
                count += 1
        return count

    
       