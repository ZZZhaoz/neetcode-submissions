class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        num_of_zero = 0
        
        for num in nums:
            total = total * num
            if num == 0:
                num_of_zero += 1
        if num_of_zero >= 2:
            return [0]*len(nums)
        list1 = []
        for i in range(len(nums)):
            if nums[i] != 0:
                list1.append(total // nums[i])
            else:
                sub = 1
            
                for i in range(len(nums)):
                    if nums[i] != 0:
                        sub = sub * nums[i]
                
                list1.append(int(sub))
        return list1
        