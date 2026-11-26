from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.post_time = 0
        # Maps userId -> list of (post_time, tweetId) in chronological order
        self.tweets = defaultdict(list)
        # Maps followerId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.post_time, tweetId))
        self.post_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        
        # Include the user's own ID so they see their own tweets
        candidates = self.following[userId] | {userId}

        # Seed the heap with the single most recent tweet from each followed user
        for followeeId in candidates:
            if self.tweets[followeeId]:
                last_idx = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][last_idx]
                # Negate time so heapq acts as a max-heap
                heapq.heappush(max_heap, (-time, tweetId, followeeId, last_idx))

        news_feed = []
        # Extract up to 10 most recent tweets
        while max_heap and len(news_feed) < 10:
            neg_time, tweetId, followeeId, idx = heapq.heappop(max_heap)
            news_feed.append(tweetId)

            # If this user has an older tweet, push the next one onto the heap
            if idx > 0:
                next_idx = idx - 1
                time, prev_tweetId = self.tweets[followeeId][next_idx]
                heapq.heappush(max_heap, (-time, prev_tweetId, followeeId, next_idx))

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # discard() safely removes without raising KeyError if not present
        self.following[followerId].discard(followeeId)
