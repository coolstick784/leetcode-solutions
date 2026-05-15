class FrontMiddleBackQueue:

    def __init__(self):
        self.q = deque([])

    def pushFront(self, val: int) -> None:
        self.q.appendleft(val)
        

    def pushMiddle(self, val: int) -> None:
        l = len(self.q)
        idx = l // 2
        self.q = list(self.q)
        self.q = deque(self.q[:idx] + [val] + self.q[idx:])


    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        print("q", self.q)
        if self.q:
            return self.q.popleft()
        return -1

    def popMiddle(self) -> int:
        
        if self.q:
            
            l = len(self.q)
            if l % 2:
                idx = l // 2
            else:
                idx = l // 2 -1
            val = self.q[idx]
            self.q = list(self.q)
            self.q = deque(self.q[:idx] + self.q[idx+1:])
            return val
        return -1

    def popBack(self) -> int:
        if self.q:
            return self.q.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
