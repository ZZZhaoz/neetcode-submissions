class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def comsume(self, piles: List[int], k: int) -> int:
            
            hour = 0
            for i in range(len(piles)):
               
                hour += math.ceil(piles[i] / k)
            return hour
       
        l, r = 1, max(piles)
        while l < r:
            m = (l + r)//2
            result = comsume(self, piles, m)
            if  result <= h:
                r = m

            else:
                l = m + 1

            # else:
            #     return m
        return l

        # def comsume(piles: List[int], k: int) -> int:
        #     hours = 0
        #     for pile in piles:
        #         # Calculate the hours needed for this pile with speed k
        #         hours += (pile + k - 1) // k  # Equivalent to math.ceil(pile / k)
        #     return hours
        
        # l, r = 1, max(piles)  # Start binary search with l = 1 (minimum valid speed)
        # while l < r:
        #     m = (l + r) // 2
        #     if comsume(piles, m) <= h:  # Check if speed m can complete eating in h hours
        #         r = m  # Try a smaller speed
        #     else:
        #         l = m + 1  # Try a larger speed
        # return l


        