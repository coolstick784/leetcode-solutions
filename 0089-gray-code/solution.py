class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        base = self.grayCode(n-1)
        old = base.copy()
        add = 2 **(n-1)
        new = []
        for idx, n in enumerate(old):
            new.append(n + add)
        new.reverse()
        return old + new


