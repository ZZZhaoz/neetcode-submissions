class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        res = []
        ps = self.permute(nums[1:])

        for p in ps:
            for i in range(len(p) + 1):
                pc = p.copy()
                pc.insert(i, nums[0])
                res.append(pc)
        return res