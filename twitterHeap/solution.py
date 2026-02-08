import heapq

class Twitter:

    def __init__(self):
        self.time = 0 #global time counter (newer tweets have bigger time stamps)
        #larger time stamps = higher priority 

        self.tweets = {} #(userid, list of tuples of (time, tweetid) )

        self.following ={} #(user x , set of users that user x follows )

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        #initialize user in tweet list if not seen before 
        if userId not in self.tweets: 
            self.tweets[userId] = []
        
        # add tweet with current time 
        self.tweets[userId].append((self.time, tweetId))
        self.time +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        #helper function to add users tweets
        def addTweet(uid): 
            if uid not in self.tweets:
                return
            #only need the last 10 tweets from each user 
            for time,tweet in self.tweets[uid][-10:]:
                #use negative time to simulate maxheap 
                heapq.heappush(heap,( -time, tweet))
            
        # add each users tweets
        addTweet(userId)
        
        # add tweets from followed users 
        if userId in self.following: 
            for followee in self.following[userId]: 
                addTweet(followee)
            
        #extract the 10 most recent tweets
        result=[]
        while heap and len(result) <10: 
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)
        return result
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: 
            return 
        
        if followerId not in self.following: 
            self.following[followerId] = set()
        
        # add followee
        self.following[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        if followerId in self.following: 
            self.following[followerId].discard(followeeId)
            #use discard since doesnt throw error if nothing is there

        
