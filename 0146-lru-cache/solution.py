class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.q = deque()
        self.ctr_keys = {}
        self.total = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dict:
            self.q.append(key)
            self.ctr_keys[key] = self.ctr_keys.get(key, 0) + 1
            return self.dict.get(key, -1)
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        self.q.append(key)

        self.ctr_keys[key] = self.ctr_keys.get(key, 0) + 1
        if key not in self.dict:
            self.total += 1
            self.dict[key] = value
            while self.total > self.capacity:
                to_remove = self.q.popleft()
                self.ctr_keys[to_remove] -= 1
                if self.ctr_keys[to_remove] == 0:
                    del self.dict[to_remove]
                    self.total -= 1
        else:
            self.dict[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
