# increasing heap with len k
# for each left in nums1, loop through every left in nums2
# while len(heap) < k, keep going
# if len(heap) == k, then check if it's greater than the max
# if it is, set the left in nums1 += 1 and set the left in nums2 to 0
# otherwise, pop the heap and keep going

# 2, 2

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [] # (-sum, num1, num2)
        max_l2 = float('inf')
        for l1 in range(len(nums1)):
            for l2 in range(len(nums2)):
                if l2 >= max_l2:
                    break
                n1 = nums1[l1]
                n2 = nums2[l2]
                s = n1 + n2
                if len(heap) < k:
                    heapq.heappush(heap, (-s, n1, n2))
                elif -s <= heap[0][0]:
                    max_l2 = l2
                    break
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-s, n1, n2))
        res = []
        while heap:
            s, n1, n2 = heapq.heappop(heap)
            res.append([n1, n2])
        res.reverse()
        return res
