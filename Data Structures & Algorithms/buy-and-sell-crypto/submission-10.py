class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 1:
        #     return 0
        l, r = 0, 1
        mini = prices[l]
        res = []
        while r < len(prices):
            if prices[r] < mini:
                mini = prices[r]
            
            res.append(prices[r] - mini)
            r += 1
        if res == []:
            return 0
        if max(res) < 0:
            return 0
        return max(res)


        