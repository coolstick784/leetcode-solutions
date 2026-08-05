class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ends = {}
        
        for idx, n in enumerate(nums):
            prev_n = ends.get(n, set()).copy()
            for num in range(-100, n):
                prev = ends.get(num, set()).copy()
                for prev_list in prev:
                    cur_list = list(prev_list)
                    cur_list.append(n)
                    ends.setdefault(n, set()).add(tuple(cur_list))
            for prev_list in prev_n:
                cur_list = list(prev_list)
                cur_list.append(n)
                ends.setdefault(n, set()).add(tuple(cur_list))
            ends.setdefault(n, set()).add(tuple([n]))

        return [list(val) for l in ends.values() for val in l if len(val) > 1]
