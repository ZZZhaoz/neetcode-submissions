class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(index, current, total):
            if total == target:
                res.append(current.copy())
                return
            if index >= len(candidates) or total > target:
                return 

            current.append(candidates[index])
            backtrack(index + 1, current, total + candidates[index])

            current.pop()
            
            while index + 1 <= len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            
            
            backtrack(index + 1, current, total)
            return 
        backtrack(0, [], 0)
        return res








                
        