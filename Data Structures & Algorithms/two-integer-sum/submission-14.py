class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = i
            else:
                if 2 * nums[i] == target:
                    return[mp[nums[i]], i]
        for i in range(len(nums)):
            if target - nums[i] in mp:
                if mp[target - nums[i]] < mp[nums[i]]:
                    return [mp[target - nums[i]], mp[nums[i]]]
                elif mp[target - nums[i]] > mp[nums[i]]:
                    return [mp[nums[i]], mp[target - nums[i]]]
            
            
        return []