# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
        
#         f = []
      
#         for num in enumerate(nums):
#             if num[0] > 0 and nums[num[0] - 1] == nums[num[0]]:
#                 continue
#             answer = []
#             l, r = num[0] + 1, len(nums) - 1
#             while l < r:
#                 if nums[l] + nums[r] < -num[1]:
#                     l += 1
#                 elif nums[l] + nums[r] > -num[1]:
#                     r -= 1
#                 else:
#                     if num[0] == l or num[0] == r:
#                         break
#                     else:
                        
#                         f.append([num[1], nums[l], nums[r]])

#                         l += 1
#                         r -= 1
#                         while l < r and nums[l + 1] == nums[l]:
#                             l += 1

#                         while r > l and nums[r - 1] == nums[r]:
#                             r -= 1
                        
                       

#         return f

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        f = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue                 # 外层 i 跳重

            l, r = i + 1, len(nums) - 1  # 双指针从 i+1 开始
            while l < r:
                s = a + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    f.append([a, nums[l], nums[r]])  # 记录一组解
                    # 先移动，再在新位置跳重；不 break，继续找同一 i 的其他解
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return f
