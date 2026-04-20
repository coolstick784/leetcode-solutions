# drink all full bottles, then exchange empty for full until we can't anymore, and continue

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        res = 0
        while full > 0 :
            res += full
            empty += full
            full = 0
            while empty >= numExchange:
                empty -= numExchange
                full += 1
                numExchange += 1
        return res


# full = 13, empty = 0, res = 0, ne = 6
# res = 13, empty = 13, full = 0 -> empty = 7, full = 1, ne = 7, empty = 0, full = 2, ne = 8, res = 15
# full = 10, empty = 0, res = 0, ne = 3, 
# res = 10, empty = 10, full = 0 -> empty = 7, ne = 4, full = 1, empty = 3, ne = 5, full = 2 
