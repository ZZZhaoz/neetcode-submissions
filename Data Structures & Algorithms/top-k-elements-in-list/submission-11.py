class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        
        for num in nums:
            if num not in table:
                table[num] = 0
            table[num] += 1
        result = []
        
        for _ in range(k):
            largest_sofar = (-1, -1)
            for num in table:
                if table[num] > largest_sofar[1]:
                    largest_sofar = (num, table[num])
            
            result.append(largest_sofar[0])
            del table[largest_sofar[0]]
            
        return result
