class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                mp = max(mp, prices[r]-prices[l])
            else:
                l = r
            r += 1
        return mp




        