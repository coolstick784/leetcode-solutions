#1. find the numbers that have squares
# then, sort those numbers largest to smallest
# we'll have a dict of answers, defaulting to 0
# if the count of the number is >= 2 and the number squared is not in the answers dict, 
# if the count of the number squared is >=  1, the ans for that number is 3
# if the count of the number squared is 0, the ans for that number is 1
#else the ans for that number is 0
# if the number squaqred is in the ans dict, and the count of the number is >=2, the ans for that number is 2 + ans[number squared]
# try for powers 2, 4, etc. until it's > the max val

# special case for 1


#[5, 4, 1, 2, 2] {5: 1, 4:1, 1:1, 2: 2}
# res = 1
# s_nums = [5, 4, 2, 1]
# 2, cur_p = 2, cur = 4, mx = 5

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ctr = Counter(nums)
        has_square = []
        res = 1
        ct_1 = ctr.get(1, 0)
        if ct_1 % 2 == 1:
            res = max(res, ct_1)
        else:
            res = max(res, ct_1-1)
        s_nums = list(set(nums))
        s_nums.sort(reverse=True)
        mx = max(nums)
        ans = {}
        for n in s_nums:
            if n == 1:
                continue
            if ctr[n] >= 2:
                cur_p = 2
                cur = n ** cur_p

                if ans.get(cur, 0) > 0:
                    ans[n] = max(ans.get(n, 0), 2 + ans[cur])
                elif ctr.get(cur, 0) > 0:
                    ans[n] = max(ans.get(n,0), 3)


        if not ans:
            return res
        res = max(res, max(ans.values()))



        return res
        
