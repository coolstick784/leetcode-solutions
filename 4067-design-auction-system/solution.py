class AuctionSystem:

    def __init__(self):
        self.heaps = {}
        self.bids = {}

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bids[(userId, itemId)] = bidAmount
        self.heaps.setdefault(itemId, [])
        heapq.heappush(self.heaps[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.bids[(userId, itemId)] = newAmount
        heapq.heappush(self.heaps[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.bids[(userId, itemId)]
        

    def getHighestBidder(self, itemId: int) -> int:
        while True:
            if not self.heaps.get(itemId):
                return -1
            cur_mx, cur_user = self.heaps[itemId][0]
            cur_mx = -1 * cur_mx
            cur_user = -1 * cur_user
            if cur_mx == self.bids.get((cur_user, itemId), -float('inf')):
                return cur_user
            heapq.heappop(self.heaps[itemId])


        


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)
