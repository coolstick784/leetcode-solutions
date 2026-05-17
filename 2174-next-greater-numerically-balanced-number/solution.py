def isBalanced(n):
    s = str(n)
    ctr = {}
    for ch in s:
        i = int(ch)
        ctr[i] = ctr.get(i, 0) + 1
    for i in ctr:
        if ctr[i] != i:
            return False
    return True

nums = []
for n in range(1,10**7+1):
    if isBalanced(n):
        nums.append(n)
        if n > 10**6:
            break


#[1, 22]
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return nums[bisect.bisect(nums, n)]    
