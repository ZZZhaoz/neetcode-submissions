class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, cur, total):
            if total == target:
                
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i = i + 1

            cur.pop()
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return res



                
        