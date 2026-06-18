class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmp = defaultdict(list)
        self.followmp = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmp[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxheap = []
       

         # Push tweets from the user and their followees
        for followee in self.followmp[userId]:
            for j, tweet in enumerate(self.tweetmp[followee]):
                # Push to heap with negative timestamp for max-heap simulation
                heapq.heappush(maxheap, [tweet[0], tweet[1], followee, j])
        for tweet in self.tweetmp[userId]:
            heapq.heappush(maxheap, [tweet[0], tweet[1]])
        
        # Get the top 10 tweets
        for _ in range(min(10, len(maxheap))):
            a = heapq.heappop(maxheap)
            if a[1] not in res:
                res.append(a[1])  # Append the tweet content
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmp[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmp[followerId]:
            self.followmp[followerId].remove(followeeId)
        
        
