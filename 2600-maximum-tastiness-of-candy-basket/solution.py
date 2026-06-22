import heapq
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        left = 0
        right = price[-1] - price[0]
        while left < right:
            med = (left + right) // 2 + 1
            start = 1
            last = price[0]
            n = 1
            while start < len(price):
                cur = price[start]
                if cur - last >= med:
                    n += 1
                    last = cur
                start += 1
            if n < k:
                right = med - 1
            else:
                left = med
                


        return left
