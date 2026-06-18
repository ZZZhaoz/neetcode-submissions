class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def comsume(self, piles: List[int], k: int) -> int:
            
            hour = 0
            for i in range(len(piles)):
               
                hour += math.ceil(piles[i] / k)
            return hour
        
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r)//2
            result = comsume(self, piles, m)
            if  result <= h:
                res = m
                r = m - 1

            else:
                l = m + 1

           
        return res

    


        