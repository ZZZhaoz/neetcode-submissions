class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 1:
        #     return 0
        l, r = 0, 1
        res = []
        minp = prices[0]
        while r < len(prices):
            if prices[r] < minp:
                minp = prices[r]
                l = r
            res.append((prices[r] - minp))

            r += 1
        if res == []:
            return 0
        return max(res)

        