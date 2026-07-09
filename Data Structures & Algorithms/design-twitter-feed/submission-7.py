class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of  [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followeeId
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []

        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                count, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minheap, [count, tweetId, followee, index - 1])
        
        while minheap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followee][index]
                heapq.heappush(minheap, [count, tweetId, followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

