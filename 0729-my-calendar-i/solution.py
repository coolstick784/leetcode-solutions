class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.intervals or self.intervals[-1][-1] <= startTime:
            self.intervals.append((startTime, endTime))
            return True

        for idx, (start, end) in enumerate(self.intervals):
            if endTime <= start:
                self.intervals.insert(idx, (startTime, endTime))
                return True
            if startTime < end:
                #print("intervals", self.intervals, "start", startTime, "end", endTime)
                return False
       
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
