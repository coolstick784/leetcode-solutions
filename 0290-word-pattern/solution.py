class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        left = 0
        map_dict = {}
        map_dict_ch = {}
        
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        while left < len(pattern):
            cur_ch = pattern[left]
            cur_word = words[left]
            if cur_word not in map_dict:
                map_dict[cur_word] = cur_ch
            elif map_dict[cur_word] != cur_ch:
                return False
            if cur_ch not in map_dict_ch:
                map_dict_ch[cur_ch] = cur_word
            elif map_dict_ch[cur_ch] != cur_word:
                return False
            left += 1
        return True
            
        
