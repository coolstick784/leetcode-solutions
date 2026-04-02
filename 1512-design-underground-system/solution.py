class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.travel = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prev = self.customers[id][0]
        prev_t = self.customers[id][1]
        total_t = self.travel.get((prev, stationName), (0, 0))[0]
        total_n = self.travel.get((prev, stationName), (0, 0))[1]
        self.travel[(prev, stationName)] = (total_t + t - prev_t, total_n + 1)

        del self.customers[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
    
        return float((self.travel[(startStation, endStation)][0]))/(self.travel[(startStation, endStation)][1])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# Each customer has its own stack
# We want a dictionary with the input, output, and time between each
# When we get the average time, get the average
