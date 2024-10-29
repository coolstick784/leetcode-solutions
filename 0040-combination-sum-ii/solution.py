class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def getSums(cur_lst, start, target):
            if target == 0:
                self.total.append(cur_lst)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                getSums(cur_lst + [candidates[i]], i + 1, target - candidates[i])

        candidates.sort()
        self.total = []
        getSums([], 0, target)
        return self.total

