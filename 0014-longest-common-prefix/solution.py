class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur_prefix = strs[0]
        len_prefix = len(cur_prefix)
        for s in strs[1:]:
            if s[:len_prefix] != cur_prefix:
                strs[0] = strs[0][:-1]
                return self.longestCommonPrefix(strs)
        return cur_prefix 
        
