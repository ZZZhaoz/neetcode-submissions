class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return[]
        res = []
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                res.append(l + 1)
                res.append(r + 1)
                return res
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
   