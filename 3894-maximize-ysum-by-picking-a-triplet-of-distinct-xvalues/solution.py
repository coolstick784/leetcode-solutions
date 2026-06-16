class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        y = [(n, idx) for idx, n in enumerate(y)]
        y.sort()
        y.reverse()
        left = 0
        middle = 1
        right = 2
        while right < len(y):
            while right < len(y) and (x[y[right][1]] == x[y[left][1]] or x[y[right][1]] == x[y[middle][1]]):
                right += 1
            if right == len(y):
                break
            while middle < right and (x[y[middle][1]] == x[y[left][1]] or x[y[middle][1]] == x[y[right][1]]):
                
                middle += 1
            if middle != right:
                break
        if right == len(y):
            return -1
        return y[right][0] + y[middle][0] + y[left][0]
        
