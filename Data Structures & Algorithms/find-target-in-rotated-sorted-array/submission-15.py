class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1
        # num = nums[0]
        # res = nums[0]
        # while l <= r:
        #     m = (l + r)//2
        #     if nums[m] < num:
        #         res = nums[m]
        #         num = nums[m]
        #         r = m - 1
        #     else:
        #         l = m + 1
        # index = nums.index(res)
        # new = nums[index:] + nums[:index] 
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = (l + r)//2
        #     if new[m] < target:
        #         l = m + 1
        #     elif new[m] > target:
        #         r = m -1
        #     else:
        #         if index + m < len(nums):
        #             return m + index
        #         else:
        #             return index + m - len(nums)
        
        # return -1


        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # Check if the left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Target is in the left half
                else:
                    l = m + 1  # Target is in the right half
            else:
                # Right half must be sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Target is in the right half
                else:
                    r = m - 1  # Target is in the left half
        return -1
        
        