import heapq
class NumberContainers:

    def __init__(self):
        self.heaps = {}
        self.idxs = {}
        self.all = {}

    def change(self, index: int, number: int) -> None:
        if index in self.all:
            prev = self.all[index]
            self.idxs[prev].remove(index)
        
        self.all[index] = number
        heapq.heappush(self.heaps.setdefault(number, []), index)
        self.idxs.setdefault(number, set()).add(index)
    def find(self, number: int) -> int:
        while self.heaps.get(number) and self.heaps[number][0] not in self.idxs[number]:
            heapq.heappop(self.heaps[number])
        if self.heaps.get(number):
            return self.heaps[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
