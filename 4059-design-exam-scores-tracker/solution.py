# we have a summed scores at each time, and we have a list of times
# on each call, do a binary search to get the sum of scores before start time and also at end time
class ExamTracker:

    def __init__(self):
        self.times = [0]
        self.scores = {0:0}

    def record(self, time: int, score: int) -> None:
        self.scores[time] = score + self.scores[self.times[-1]]
        self.times.append(time)
        
        

    def totalScore(self, startTime: int, endTime: int) -> int:
        prev_time = self.scores[self.times[bisect.bisect_left(self.times, startTime) - 1]]
        end_time = self.scores[self.times[bisect.bisect_right(self.times, endTime) - 1]]
        return end_time-prev_time


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)


# [0, 1], {0:0, 1:98}
# [0, 1, 5], {0:0, 1:98, 5:197}
