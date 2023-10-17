class Twitter:

    def __init__(self):
        self.follows = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        if userId in self.follows:
            following = self.follows[userId]
        else:
            following = None
        for tweet in self.tweets[-1::-1]:
            tweeter, tweetId = tweet
            if (following and tweeter in following) or tweeter == userId:
                feed.append(tweetId)
            if len(feed) == 10:
                break
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)