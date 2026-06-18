class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap  =[]
        i = 0
        for ls in points:
            heapq.heappush(heap, (ls[0]* ls[0]+ ls[1]* ls[1], i))
            i += 1
        res = []
        j = 0
        # a = heapq.heappop(heap)
        while j < k:
            a = heapq.heappop(heap)
            res.append(a[1])
            j += 1
        
        # resint = a[0]
        # if heap:
        #     b = heapq.heappop(heap)
        #     while b[0] == resint:
        #         res.append(a[1])
        #         b = heapq.heappop(heap)
        final = []
        for num in res:
            final.append(points[num])
        return final

        

        
        