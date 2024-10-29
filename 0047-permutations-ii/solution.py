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
    def permuteUnique(self, nums):
        mapping = {}
        for idx, num in enumerate(nums):
            mapping[idx] = num
        og_combos = self.permute(list(mapping.keys()))
        #print("og", og_combos)
        for idx, l in enumerate(og_combos):
            for idx2, v in enumerate(l):
                og_combos[idx][idx2] = mapping[v]
        #print("mapping", mapping)
        fin = []
        for l in og_combos:
            if l not in fin:
                fin.append(l)
        return fin

