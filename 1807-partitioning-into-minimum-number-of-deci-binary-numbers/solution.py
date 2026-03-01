class Solution:
    def minPartitions(self, n: str) -> int:
        ints = [int(ch) for ch in str(n)]
        return max(ints)
