from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ctr = Counter(nums)
        nums.sort()
        new = []
        for idx, n in enumerate(nums):
            if idx <= 3:
                new.append(n)
            elif n != nums[idx-3]:
                new.append(n)

        print("new", new)

        ns = set([])
        res = []
        sols = set([])
        for idx in range(len(new)):
            n1 = new[idx]
            for idx2 in range(idx+1, len(new)):
                
                n2 = new[idx2]
                s = n1 + n2
                goal = -s
                if goal in ns:
                    cur = sorted([n1, n2, -s])
                    sol = str(cur[0]) + "," + str(cur[1]) + "," + str(cur[2]) 
                    if sol not in sols:
                        res.append(cur)
                        sols.add(sol)
            ns.add(n1)
        
        return res

        

        
