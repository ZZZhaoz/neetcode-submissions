class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        index = nums.index(res)
        new = nums[index:] + nums[:index] 
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if new[m] < target:
                l = m + 1
            elif new[m] > target:
                r = m -1
            else:
                if index + m < len(nums):
                    return m + index
                else:
                    return index + m - len(nums)
        
        return -1
            
        
        