import bisect
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.idxs = {}
        for idx, n in enumerate(arr):
            self.idxs.setdefault(n, []).append(idx)
        

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.idxs:
            return 0
        return bisect.bisect(self.idxs[value], right) - bisect.bisect_left(self.idxs[value], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
