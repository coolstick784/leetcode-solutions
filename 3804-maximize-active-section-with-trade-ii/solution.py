# for each query, we want to know
# 1. the number of 1s
# 2. the max number of 0s in a group
# 3. the max number of two consecutive 0 groups
# 4. the min number of 1s in a group

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ends = {}
        total = Counter(s)['1']
        ans = [None for _ in queries]
        for idx, (start, end) in enumerate(queries):
            ends.setdefault(end, []).append((start, idx))
        #print("ends", ends)
        ctr = [0]
        zero_groups = [] # descending
        zero_idxs = []
        two_zero_groups = [] # descending
        two_zero_idxs = []
        one_groups = [] # ascending
        one_idxs = []
        prev_ch = None
        prev_ct = 0
        for idx, ch in enumerate(s):
            #print("idx", idx, "ch", ch)
            if ch == "1":
                ctr.append(ctr[-1] + 1)
                cur_ct = 1
                if ch == prev_ch:
                    cur_ct = prev_ct + 1
                else:
                    if prev_ch == '0':
                        if zero_groups:
                            two_zero = prev_ct + zero_groups[-1]
                            prev_idx = zero_idxs[-1]
                            while two_zero_groups and two_zero >= two_zero_groups[-1]:
                                two_zero_groups.pop()
                                two_zero_idxs.pop()
                            two_zero_groups.append(two_zero)
                            two_zero_idxs.append(prev_idx)

                        while zero_groups and prev_ct >= zero_groups[-1]:
                            zero_groups.pop()
                            zero_idxs.pop()
                        zero_groups.append(prev_ct)
                        zero_idxs.append(start_idx)

                    start_idx = idx

            else:
                ctr.append(ctr[-1])
                cur_ct = 1
                if ch == prev_ch:
                    cur_ct = prev_ct + 1
                else:

                    if prev_ch == "1":
                        while one_groups and prev_ct <= one_groups[-1]:
                            one_groups.pop()
                            one_idxs.pop()
                        one_groups.append(prev_ct)
                        one_idxs.append(start_idx)
                    start_idx = idx
                
            #print("zero groups", zero_groups, "one groups", one_groups, "zero idxs", zero_idxs, "one idxs", one_idxs, "ctr", ctr)
            prev_ch = ch
            prev_ct = cur_ct
            for start, i in ends.get(idx, []):
                base = total
                # max 0 can either be the first one after being cut off, the 2nd one, or the current count
                # max two zeros can either be first + second, second + third, first + cur, or second + cur
                if not zero_idxs or not one_idxs:
                    ans[i] = base
                    continue
                start_zero_idx = bisect.bisect(zero_idxs, start) - 1
                sub = (start - zero_idxs[start_zero_idx])

                first_zero = min(max(0, zero_groups[start_zero_idx] - sub), zero_groups[start_zero_idx])
                if start_zero_idx + 1 < len(zero_groups):
                    second_zero = zero_groups[start_zero_idx+1]
                else:
                    second_zero = 0
                cur_zero = 0
                if ch == "0":
                    cur_zero = cur_ct
                #print(first_zero, second_zero, cur_zero)
                
                max_zero = max(first_zero, second_zero, cur_zero)


                start_two_zero_idx = bisect.bisect(two_zero_idxs, start) - 1
                if start_two_zero_idx >= 0:
                    first_two_zero = max(0, two_zero_groups[start_two_zero_idx] - (start - two_zero_idxs[start_two_zero_idx]))
                else:
                    first_two_zero = 0
                if start_two_zero_idx + 1 < len(two_zero_groups):
                    second_two_zero = two_zero_groups[start_two_zero_idx+1]
                else:
                    second_two_zero = 0
                
                max_two_zero = max(first_two_zero, second_two_zero)


                if not zero_idxs:
                    prev_zero = 0
                elif zero_idxs[-1] >= start:
                    prev_zero = zero_groups[-1]
                else:
                    prev_zero = max(0, zero_groups[-1] - (start-zero_idxs[-1]))
                
                max_two_zero = max(max_two_zero, cur_zero + prev_zero)
                #print("i", i, "max zero", max_zero, "max two zero", max_two_zero)


                start_one_idx = bisect.bisect(one_idxs, start)
                if start_one_idx < len(one_idxs):
                    first_one = one_groups[start_one_idx]
                else:
                    first_one = float('inf')


                min_one = first_one
                if first_one == float('inf'):
                    ans[i] = base
                    continue



                ans[i] = max(base, base + max_zero - min_one, base + max_two_zero, 1)
        return ans
                

