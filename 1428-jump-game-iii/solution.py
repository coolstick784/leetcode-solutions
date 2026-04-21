class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        explored = set()
        values_0 = set([idx for idx, n in enumerate(arr) if n == 0])
        self.ctr = 0
        def explore(idx):
            
            if idx in explored or idx < 0 or idx >= len(arr):
                return False
            explored.add(idx)
            if idx in values_0:
                return True
            return explore(idx + arr[idx]) or explore(idx - arr[idx])
        return explore(start)

