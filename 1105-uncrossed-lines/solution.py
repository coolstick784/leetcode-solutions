class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        # dynamic programming
        # for each number, consider each index it can draw a line to
        # if the top is > and bottom is < , or top is < and bottom is >, then two lines are crossing
        # at each top index, we need to determine if we want to draw a line or not
        # if we do, we have to determine the best number to draw a line to
        # at most 25k combos


        # [4, 2, 1, 3, 10]
        # [5, 6, 1, 4, 2]
        # for the leftmost one, we want the cloest match to the left, either that or not drawing a line
        # then, for the second one, we either want the closest to the left, or not draw a line
        # and so on
        # once we move to the right in either the top or bottom, we can't go back
        # there is a best score for each combination, if we start at a top/bottom index combo
        # so use an LRU cache for the best score, and try to compare either moving to the right one in the top (not matching) or moving to the right
        #one in the top and moving to the match + 1 in the bottom

        idxs1 = {}
        idxs2 = {}
        for idx, n in enumerate(nums1):
            idxs1.setdefault(n, []).append(idx)
        for idx, n in enumerate(nums2):
            idxs2.setdefault(n, []).append(idx)      
        @lru_cache(None)
        def best(top, bottom):
            if bottom == len(nums2) or top == len(nums1):
                return 0

            top_n = nums1[top]
            if top_n not in idxs2 or idxs2[top_n][-1] < bottom:
                return best(top+1, bottom)
            if bottom in idxs2[top_n]:
                return 1+best(top+1, bottom+1)
            
            bottom_n = idxs2[top_n][bisect.bisect(idxs2[top_n], bottom)]

            return max(best(top+1, bottom), 1+best(top+1, bottom_n+1))
        return best(0, 0)

