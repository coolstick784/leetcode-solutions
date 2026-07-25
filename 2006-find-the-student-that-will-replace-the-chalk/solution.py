class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        k = k % sum(chalk)
        for idx, c in enumerate(chalk):
            if k < c:
                return idx
            k -= c
