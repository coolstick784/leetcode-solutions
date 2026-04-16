# [1, -2, 4, -8, 16, -32, 64, -128...]
# start from 8 and find -1, or start from 4 and find 3
# start from 4 and find -5, or start from -2 and find 1

# we'll want the sum of all negatives up to that point 
# at each point, we can either include or not include it
# starting from the one higher than it 
# so we have a starting point, and a number to get to
# if it's greater than all the positives up to that point, or less than all the negatives, it's not possible


cur = [1]
while cur[-1] <= 10**10:
    cur.append(cur[-1] * -2)
pos_sum = []
neg_sum = []
for n in cur:
    if pos_sum and n > 0:
        pos_sum.append(pos_sum[-1] + n)
        neg_sum.append(neg_sum[-1])
    elif n > 0:
        pos_sum = [n]
        neg_sum = [0]
    elif n < 0:
        neg_sum.append(neg_sum[-1] + n)
        pos_sum.append(pos_sum[-1])
positives = [n for n in cur if n > 0]

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        def solve(cur_n, position):
            if position < 0:
                return "" if cur_n == 0 else False
            if cur_n == cur[position]:

                return "1" + solve(0, position-1)
                
            if cur_n == 0:
                return "0" + solve(0, position-1)
            if cur_n > 0 and cur_n > pos_sum[position]:
                return False
            if cur_n < 0 and cur_n < neg_sum[position]:
                return False

            include = solve(cur_n-cur[position], position-1)
            if include:
                return "1" + include
            exclude = solve(cur_n, position-1)
            return "0" + exclude

        pos = bisect.bisect_left(positives, n)*2 + 2
        return solve(n, pos).lstrip("0")
        
