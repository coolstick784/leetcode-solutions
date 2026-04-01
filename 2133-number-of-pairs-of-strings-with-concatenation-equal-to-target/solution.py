class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        ctr = Counter(nums)
        res = 0
        for s in ctr:
            if len(s) > len(target):
                continue
            ans = set()
            if target.startswith(s):
                left = target[len(s):]

                if left in ctr:
                    if left == s:
                        ans.add((left, ctr[left] * (ctr[left]-1)))
                    else:
                        ans.add((left, max(1, ctr[s] * (ctr[left]))))

   
            res += sum([a[1] for a in ans])
        return res
