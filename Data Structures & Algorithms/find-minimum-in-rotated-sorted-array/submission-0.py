class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        num = nums[0]
        res = nums[0]
        while l <= r:
            m = (l + r)//2
            if nums[m] < num:
                res = nums[m]
                num = nums[m]
                r = m - 1
            else:
                
                l = m + 1
        return res
            



        