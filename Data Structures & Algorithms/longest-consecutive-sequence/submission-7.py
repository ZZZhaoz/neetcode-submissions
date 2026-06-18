class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            m[num] = 1
        res = []
        for k, v in m.items():
            count = 1
            while k - 1 in m:
                k-=1
            while k + 1 in m:
                k+=1
                count+=1
            res.append(count)
        if nums == []:
            return 0
        return max(res)
                