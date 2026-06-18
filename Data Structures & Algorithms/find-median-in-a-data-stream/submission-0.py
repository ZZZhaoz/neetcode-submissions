class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if  len(self.maxheap) != 0 and -num > self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        if len(self.maxheap) > len(self.minheap):
            a = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -1*a)
        elif (len(self.minheap) - len(self.maxheap)) > 1:
            a = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1*a)
        

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return ((-1*self.maxheap[0] + self.minheap[0]) / 2)
        else:
            return self.minheap[0]
        
        