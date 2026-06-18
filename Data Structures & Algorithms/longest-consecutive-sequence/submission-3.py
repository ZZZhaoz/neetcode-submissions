class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        res = []
        diction = {}
        for num in nums:
            if num not in diction:
                diction[num] = 1
            # if num + 1 or num - 1
            #     diction[num-1] = 1
            #     diction[num-+] = 1
        largest = 0
        r = 0
        for key in diction:
            i = 0
            while key + i in diction:
                
                i += 1
                
           
            res.append(i)
                
           
        
        return max(res)




        