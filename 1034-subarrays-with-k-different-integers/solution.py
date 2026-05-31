class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left= 0
        lr = 0
        right = 0
        s = set()
        ctr = {}
        res = 0
        while right < len(nums):
            n = nums[right]
            s.add(n)
            ctr[n] = ctr.get(n, 0) + 1
            

            if len(s) > k:
                left = lr
                s.remove(nums[lr-1])
            if len(s) == k:

                while len(ctr.keys()) == k:
                    l = nums[lr]
              
                    ctr[l] -= 1
                    lr += 1
                    if ctr[l] == 0:
                        del ctr[l]
                res += (lr-left)




            right += 1

        return res
