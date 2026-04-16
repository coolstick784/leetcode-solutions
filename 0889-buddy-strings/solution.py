#lf the lenths are not equal, return False
#loop through each letter
#if the letters match, move on
#otherwise, note the indices where they don't match
#if there are exactly 2 indices that don't match, and flipping them would set them equal, return True
# otherwise, return False

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        ctr = Counter(s)
        not_equal = []
        for idx, ch in enumerate(s):
            if ch != goal[idx]:
                not_equal.append((idx, ch))
            if len(not_equal) > 2:
                return False
        if len(not_equal) == 0 and max(ctr.values()) > 1:
            return True
        if len(not_equal) != 2:
            return False
        idx1 = not_equal[0][0]
        ch1 = not_equal[0][1]
        idx2 = not_equal[1][0]
        ch2 = not_equal[1][1]
        g1 = goal[idx1]
        g2  = goal[idx2]
        if ch2 == g1 and ch1 == g2:
            return True
        return False
        
