# sort then reverse
# as long as citations[idx] >= idx+1, add 1 to res

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        res = 0
        for idx, c in enumerate(citations):
            if c >= (idx+1):
                res += 1
        return res
        
