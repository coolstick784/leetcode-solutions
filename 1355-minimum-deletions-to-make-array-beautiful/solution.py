class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        prev = None
        kept_len = 0

        for n in nums:
            if kept_len % 2 == 0:
                prev = n
                kept_len += 1
            else:
                if prev != n:
                    kept_len += 1
                else:
                    deletions += 1

        if kept_len % 2 == 1:
            deletions += 1

        return deletions
