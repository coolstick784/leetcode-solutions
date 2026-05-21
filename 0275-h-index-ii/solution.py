# num papers = len(citations)
# want to find the lowest idx that is valid
# if citations[idx] >= ((num papers) - idx)  , then (num papers) - idx is valid
# if citations[idx] < (num papers) - idx, we move to the right
# if citations[idx] >= ((num papers) - idx), note that our best is num papers - idx, but try moving to the left

# [1, 2, 2, 4] ans = 2
# left = 0, right = 3
# left = 2, right = 3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        best = 0
        left = 0
        right = len(citations) -1
        papers = len(citations)
        while left <= right:
            med = (left + right) // 2
            cur = papers - med
            if citations[med] < cur:
                left = med + 1
            else:
                best = max(best, cur)
                right = med - 1

        return best 
        
