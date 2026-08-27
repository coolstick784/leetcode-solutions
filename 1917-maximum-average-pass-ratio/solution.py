import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for p, t in classes:
            heapq.heappush(heap, (-((p+1)/(t+1) - (p/t)), t, p))
        for _ in range(extraStudents):
            _, t, p = heapq.heappop(heap)
            heapq.heappush(heap, (-((p+2)/(t+2) - (p+1)/(t+1)), t+1, p+1))
        print(heap)
        return sum([p/t for _, t, p in heap]) / len(heap)
