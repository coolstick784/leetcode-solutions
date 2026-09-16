class TimeMap:

    def __init__(self):
        self.keys = {}
        self.timestamps = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys.setdefault(key, []).append(timestamp)
        self.timestamps[(key, timestamp)] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.keys.get(key) or self.keys[key][0] > timestamp:
            return ""
        idx = bisect.bisect(self.keys[key], timestamp) - 1
        t = self.keys[key][idx]
        return self.timestamps[(key, t)]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
