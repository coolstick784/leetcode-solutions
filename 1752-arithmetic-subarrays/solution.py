class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isSorted(cur):
            if len(cur) <= 2:
                return True
            cur.sort()
            base = cur[0]
            diff = cur[1] - cur[0]
            for idx, n in enumerate(cur):
                if idx <= 1:
                    continue
                if n - cur[idx-1] != diff:
                    return False
            return True
            
        res = []
        for idx in range(len(l)):
            left = l[idx]
            right = r[idx]
            cur = nums[left:right+1]
            if isSorted(cur):
                res.append(True)
            else:
                res.append(False)
        return res

