class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        sub = []
        nums.sort()
        def bc(i):
            if i > len(nums) - 1:
                if sub not in answer:
                    answer.append(sub.copy())
                return
            
            sub.append(nums[i])
            bc(i + 1)
            sub.pop()
            bc(i + 1)
        
        bc(0)
        return answer
