class Solution:
    
                

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(self, nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (r + l)//2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m

            return -1
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            m = (l+r)//2
            if matrix[m][-1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
               break
        # if matrix[m][0] < target:
        #     # if m < len(matrix) - 1:
        #     #      b = search(self, matrix[m + 1], target)
        #     b = -1
        #     a = search(self, matrix[m], target)
        #     if (a or b) != -1:
        #         return True
        #     return False

        # elif matrix[m][0] > target:
        #     # if m > 0:
        #     #     b= search(self, matrix[m - 1], target)
        #     b = -1
        a = search(self, matrix[m], target)
        if a != -1:
            return True
        return False
        # else:
        #     return True
            



        


            

        
        
        