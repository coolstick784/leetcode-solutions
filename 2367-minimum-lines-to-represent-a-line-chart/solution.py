import numpy as np 
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 2:
            return len(stockPrices) - 1
        stockPrices.sort()
        lines = 1
        last_slope = np.longdouble(np.longdouble(stockPrices[1][1] - stockPrices[0][1]) /  np.longdouble(stockPrices[1][0] - stockPrices[0][0]))
        print("yc", (stockPrices[1][1] - stockPrices[0][1]))
        print("xc", (stockPrices[1][0] - stockPrices[0][0]))
        last_x = stockPrices[1][0]
        last_y = stockPrices[1][1]
        for x, y in stockPrices[2:]:
            slope = np.longdouble(np.longdouble(y-last_y) / np.longdouble(x-last_x))
            print("yc", y-last_y)
            print("xc", x-last_x)
            print("slope", slope)
            print("last slope", last_slope)
            if slope != last_slope:
                lines += 1

            last_x = x
            last_y = y
      
            last_slope = slope
        return lines
