
class DataStream:

    def __init__(self, value: int, k: int):
        self.streak = 0
        self.value = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.streak = 0
        else:
            self.streak += 1
        return self.streak >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
