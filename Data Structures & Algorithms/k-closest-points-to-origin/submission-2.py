class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dlist = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            dlist.append([distance, point[0], point[1]])

        heapq.heapify(dlist)
        res = []
        while k > 0:
            d, x, y = heapq.heappop(dlist)
            res.append([x, y])
            k -= 1

        return res

        