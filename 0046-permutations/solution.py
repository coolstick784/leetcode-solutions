class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.combos = [[n] for n in nums]
        num_iters = 0
        while num_iters < len(nums) - 1:
            cur_combos = []
            for combo in self.combos:
                other = [[n] for n in nums if n not in combo]
                for o in other:
                    
                    cur_combos.append(combo + o)


            self.combos = cur_combos.copy()
            num_iters += 1
        return self.combos
