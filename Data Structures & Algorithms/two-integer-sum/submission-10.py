class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        i = 0
        for num in nums:
            if num in table:
                if 2 * num == target:
                    return [table[num], i]
            else:
                table[num] = i
            
            if target - num in table and table[target - num] != i:
                if i < table[target - num]:
                    return [i, table[target - num]]
                else:
                    return [table[target - num], i] 
            

            i += 1
            