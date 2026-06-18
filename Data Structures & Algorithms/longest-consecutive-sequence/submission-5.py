class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        mp = {}
        for num in nums:
            if num not in mp:
                mp[num] = 1
        largest = 0
        for key in mp:
            if key - 1 not in mp:
                cnt = 0
                while key in mp:
                    key += 1
                    cnt += 1
                if cnt > largest:
                    largest = cnt
                
        return largest




        