class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        res = []
        perms = self.permute(nums[1:])
        a = nums[0]
        for perm in perms:
            for i in range(len(perm) + 1):
                pc = perm.copy()
                pc.insert(i, a)
                res. append(pc)
        return res
        