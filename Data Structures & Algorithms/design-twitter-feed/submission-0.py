class Twitter:

    # this is a rough first pass, should probably have reverse map and get rid of posts_set
    # also we can store (nth, tweetId, ownerId) to make things simpler
    def __init__(self):
        self.posts = defaultdict(deque) # userId to one or many tweetIds (posts)
        self.posts_set = defaultdict(set)
        self.user_feeds = defaultdict(deque) # userId to one or many tweetIds (feed)
        self.connections = defaultdict(set) # userId to one or many userId
        self._nth = 0 # tracks post order

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._nth -= 1
        curr_tweet = (self._nth, tweetId)
        # update userId posts
        self.posts[userId].appendleft(curr_tweet)
        self.posts_set[userId].add(curr_tweet)
        # update userId feed
        self.user_feeds[userId].appendleft(curr_tweet)
        # update connection(s) feed
        for curr_id, follows in self.connections.items():
            if userId in follows:
                self.user_feeds[curr_id].appendleft(curr_tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        for _, tweetId in self.user_feeds[userId]:
            if len(out) == 10:
                break
            out.append(tweetId)
        
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId not in self.connections[followerId]:
            self.connections[followerId].add(followeeId)
        else:
            return
        # This is roughly O(n + m) because Python uses tim-sort 
        new_feed = sorted(self.user_feeds[followerId] + self.posts[followeeId])
        self.user_feeds[followerId] = deque(new_feed)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.connections[followerId]:
            self.connections[followerId].remove(followeeId)
        else:
            return
        
        new_feed = deque()
        for post in self.user_feeds[followerId]:
            if post not in self.posts_set[followeeId]:
                new_feed.append(post)

        self.user_feeds[followerId] = new_feed