class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1)
        cur = 1
        for n in nums:
            cur *= n
            left.append(cur)

        right = []
        right.append(1) 
        cur = 1
        for n in nums[::-1]:
            cur *= n
            right.append(cur)
        right.reverse()
        left = left[:-1]
        right = right[1:]
        print("left", left)
        print("right", right)
        res = []
        for idx, l in enumerate(left):
            res.append(l * right[idx])
        return res
            
