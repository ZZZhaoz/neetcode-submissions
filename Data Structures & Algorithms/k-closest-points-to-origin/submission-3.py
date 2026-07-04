class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        d= []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heap.append([distance, point[0], point[1]])

        heapq.heapify(heap)
        res = []
        i = 0
        while i < k:
            a = heapq.heappop(heap)
            res.append([a[1], a[2]])
            i+= 1
        
        return res


        