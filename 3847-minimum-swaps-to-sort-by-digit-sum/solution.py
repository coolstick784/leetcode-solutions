#  [18,43,34,16]
# [(7, 16, 3), (7, 34, 2), (7, 43, 2), (9, 18, 0)] new dict = { 16:0, 34:1, 43: 2, 18: 3}
# []


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        new = [] # (sum, number, original idx)
        # when we swap, we'll need to change the original idx of the number we swap with

        @lru_cache(None)
        def get_sum(num):
            cur = 0
            while num > 0:
                cur += num % 10
                num //= 10
            return cur

        for idx, n in enumerate(nums):
            cur_s = get_sum(n)
            new.append((cur_s, n, idx))
        new.sort()
        new_dict = {}
        for idx, (cur_s, n, old_idx) in enumerate(new):
            new_dict[n] = idx


        
        res = 0
        idx = 0
        for cur_s, n, old_idx in new:
            if old_idx != idx:
                res += 1
                old_num = nums[idx]
                new_idx_of_old = new_dict[old_num]
                new[new_idx_of_old] = (get_sum(old_num), old_num, old_idx)
                nums[idx] = n
                nums[old_idx] = old_num

            idx +=  1
        return res
