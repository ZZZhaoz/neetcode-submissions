class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        answer = []
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                answer.append(l + 1)
                answer.append(r + 1)
                break
            

        return answer

        