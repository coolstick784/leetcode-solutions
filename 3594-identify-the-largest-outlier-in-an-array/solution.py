class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        s = sum(nums)
        
        for n in range(1000, -1001, -1):
            if n not in ctr:
                continue
            cur_s = s - n
            for p in range(1000, -1001, -1):
                if p not in ctr:
                    continue
                if cur_s - p == p and (p != n or ctr[p] >= 2):
                    
                    return n
                

