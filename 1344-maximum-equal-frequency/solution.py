# at each prefix we should count the number of distinct elements that have appearewd
# also, we should have a dict with count: num
# then, we can either say e.g at idx 17 with 5 distinct elements, it must be 4 * 4 with one extra, or 5 4 4 4 with 4 distinct

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        explored = set()
        res = 0
        counts = {}
        rev_counts = {}
        for idx, n in enumerate(nums):
            explored.add(n)
            distinct = len(explored)
            prev_ct = rev_counts.get(n, 0)
            rev_counts[n] = prev_ct + 1
            if prev_ct != 0:
                counts[prev_ct].remove(n)
            counts.setdefault(prev_ct+1, set()).add(n)

            ct = idx + 1
            if (ct - 1) % distinct == 0:
           
                goal = (ct-1) // distinct


                if len(counts.get(goal, set())) == distinct - 1 and (len(counts.get(goal+1, set())) == 1):
                    res = ct
                    
            if distinct > 1 and (ct-1) % (distinct-1) == 0:

                goal = (ct-1) // (distinct-1)
                if goal == 1 and (ct-1) == (distinct-1):
                    res = ct
                elif len(counts.get(goal, set())) == distinct - 1 and (len(counts.get(1, set())) == 1):
                    res = ct

        return res
                
