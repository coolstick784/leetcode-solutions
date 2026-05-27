class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:

        if key in self.od:
            self.od.move_to_end(key)
        return self.od.get(key, -1)
    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)

        elif len(self.od) == self.capacity:
            self.od.popitem(last=False)
        self.od[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
