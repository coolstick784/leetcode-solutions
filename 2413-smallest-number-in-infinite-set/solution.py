class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()
        self.min = 1

    def popSmallest(self) -> int:
        out = self.min
        self.removed.add(out)
        while self.min in self.removed:
            self.min += 1
        return out

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
        self.min = min(self.min, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
