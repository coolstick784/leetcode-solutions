class MapSum:

    def __init__(self):
        self.pre = {}
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.pre
        if key in self.keys:
            prev = self.keys[key]
        else:
            prev = 0
        for idx, ch in enumerate(key):
            cur.setdefault(ch, {})
            cur[ch]['val'] = cur[ch].get('val', 0) + val - prev
            cur = cur[ch]
        self.keys[key] = val


    def sum(self, prefix: str) -> int:
        cur = self.pre
        
        for idx, ch in enumerate(prefix):
       
            if ch in cur:
                cur = cur[ch]
            else:
                return 0
        return cur['val']


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
