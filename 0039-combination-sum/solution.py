class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def getSums(cur_lst, candidates, target):
            if target == 0:
                self.total.append(cur_lst)
                return
            for i, c in enumerate(candidates):
                if c <= target:
                    getSums(cur_lst + [c], candidates[i:], target - c)

        self.total = []
        getSums([], candidates, target)
        return self.total

