class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.validTokens = 0
        self.ttl = timeToLive
        self.queue = deque([])
        self.tokens = {}
    def removeExpired(self, currentTime):
        while self.queue and self.queue[0][1] <= currentTime:
            token, time = self.queue.popleft()
            self.tokens[token] -= 1
            if self.tokens[token] == 0:
                self.validTokens -= 1
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.removeExpired(currentTime)
        self.queue.append((tokenId, currentTime+self.ttl))
        self.tokens[tokenId] = 1
        self.validTokens += 1


        

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.removeExpired(currentTime)
        if self.tokens.get(tokenId, 0) >= 1:
            self.tokens[tokenId] += 1
            self.queue.append((tokenId, currentTime+self.ttl))
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
      
        self.removeExpired(currentTime)

        return self.validTokens
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

# we want a queue of tokens, with their expiration time
# we also want a dictionary of each token, with the count it has in our queue
# the queue should be sorted by most recent expiration date
# when we generate a token, we add it to the end of the queue, and we add 1 to our unexpired tokens number, and we set that value in the dictionary to 1
# when we renew a token, we first check if the dictionary value of it (use get incase it uses one that hasn't been generated) is >= 1. if it is, add 1 to that counter,
# but don't add 1 to the number of unexpired tokens
# whenever any function call is made, we first need to call removeExpired(self, currentTime), which removes all expired tokens. this first subtracts 1 from that token in the dictionary,
# and also if that value becomes 0, subtracts the number of unexpired otkens by 1
# when we count unexpired tokens, simply return the unexpired token count
