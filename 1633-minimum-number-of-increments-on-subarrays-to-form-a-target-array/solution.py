class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        running = 0
        for idx, n in enumerate(target):
            if n >= running:
                res += (n - running)
                running = n
            else:
                running = n
        return res
