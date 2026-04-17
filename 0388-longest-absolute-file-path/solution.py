# we want the length of each current level
# go through the string until we find a \n
# the first group starts at level 0
# then, the number of \t's before an element is the level it is on, e.g. \t\t means level 2
# then, the length of our level is equal to len(level-1) + len(cur name)
# then, if our current name has a "." in it, our res is the max of (cur res, len(level) + level number), e.g. if it's level 1 it'll have one /
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        levels = {0:0}
        cur_level = 0
        is_end = False
        res = 0
        for idx, ch in enumerate(input):
            if ch == "\n":
                is_end = False
                cur_level = 0
                if input[idx+1] != "\t":
                    levels[0] = 0
            elif ch == "\t":
                cur_level += 1
                if input[idx+1] != "\t":
                    levels[cur_level] = levels[cur_level-1]
            else:
                levels[cur_level] += 1
                if ch == ".":
                    is_end = True
                if is_end and (idx == len(input) -1 or input[idx+1] == "\n"):
                    res = max(res, levels[cur_level] + cur_level)
            
        return res
            
        
