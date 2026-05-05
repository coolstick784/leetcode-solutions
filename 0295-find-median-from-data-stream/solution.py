# 2 heaps, one with the lower half (possibly one more than the upper half) descending and one with the upper half (possibly one less than the lower half) ascending
# if the lengths are equal, and either both are empty or it's between the upper and lower (inclusive), or it's < the max of the min, add the number to the min heap
# if the lengths are equal, and it's > the min of the max heap, add it to the max heap, and add the lowest from the max heap to the min heap
# if the length are not equal, then min must be 1 more than max
# if the lengths are not equal, and it's >= the max of the min heap, add it to the max heap
# otherwise, add it to the min heap, and add the highest from the min heap to the max heap
# to get the median, if the lengths are equal, it's the average of the max from min and min from max
# if they're not equal, it's the max from min


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            if self.min_heap == [] or num <= self.max_heap[0]:
                heapq.heappush(self.min_heap, -num)
            else:
                heapq.heappush(self.max_heap, num)
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        else:
            if num >= -self.min_heap[0]:
                heapq.heappush(self.max_heap, num)
            else:
                heapq.heappush(self.min_heap, -num)
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.min_heap[0] +self.max_heap[0]) / 2
        return -self.min_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
