class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {} # key: (ctr, value)
        self.heap = [] # (ctr, key)
        self.ctr = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not self.dict.get(key):
            return -1
        self.ctr += 1
        heapq.heappush(self.heap, (self.ctr, key))
        _, val = self.dict[key]
        self.dict[key] = (self.ctr, val)
        return self.dict[key][1]
        

    def put(self, key: int, value: int) -> None:
        self.ctr += 1
        self.dict[key] = (self.ctr, value)
        while self.heap and self.dict[self.heap[0][1]][0] != self.heap[0][0]:
            heapq.heappop(self.heap)
        if len(self.dict.keys()) > self.capacity:
            _, p_key = heapq.heappop(self.heap)
            del self.dict[p_key]
        heapq.heappush(self.heap, (self.ctr, key))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
