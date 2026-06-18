class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        f = []
      
        for num in enumerate(nums):
            if num[0] > 0 and nums[num[0] - 1] == nums[num[0]]:
                continue
            answer = []
            l, r = num[0] + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < -num[1]:
                    l += 1
                elif nums[l] + nums[r] > -num[1]:
                    r -= 1
                else:
                    f.append([num[1], nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

                    while r > l and nums[r + 1] == nums[r]:
                        r -= 1
                        
                       

        return f