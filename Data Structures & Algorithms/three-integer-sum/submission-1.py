class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            res = []
            target = -(nums[i])
            l, r = i + 1, len(nums) - 1
            while l < r:
                # if nums[l] + nums[r] == target:
                #     res.append(nums[l])
                #     res.append(nums[r])
                #     res.append(target)
                #     if res.sort() not in result:
                #         result.append(res.sort())
                #         continue
                if nums[l] + nums[r] == target:
                    triplet = [nums[i], nums[l], nums[r]]
                    result.append(triplet)
                    # Skip duplicates for the second and third numbers
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # Move pointers after processing
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l +=1
                else:
                    r -= 1
        return result

        