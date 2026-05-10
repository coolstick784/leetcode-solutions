class LFUCache:

    def __init__(self, capacity: int):
        self.heap = [] # frequenctly -> recency -> key
        self.ctr = 0
        self.cache = {} # [value, use counter, most recent use]
        self.capacity = capacity
        

    def get(self, key: int) -> int:
     
        self.ctr += 1
        out = self.cache.get(key, [-1, 0, 0])[0]
        if out != -1:
            self.cache[key][1] += 1
            self.cache[key][2] = self.ctr
        return out
        

    def put(self, key: int, value: int) -> None:
        self.ctr += 1
        if key in self.cache:
            self.cache[key][1] += 1
            self.cache[key][0] = value
            self.cache[key][2] = self.ctr
            return
        
        if len(self.cache.keys()) == self.capacity:
            found = False
            while not found:
                freq, rec, k = heapq.heappop(self.heap)
                if rec == self.cache[k][2]:
                    del self.cache[k]
                    found = True
                else:
                    heapq.heappush(self.heap, (self.cache[k][1], self.cache[k][2], k))\

        self.cache[key] = [value, 1, self.ctr]
        heapq.heappush(self.heap, (1, self.ctr, key))

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
