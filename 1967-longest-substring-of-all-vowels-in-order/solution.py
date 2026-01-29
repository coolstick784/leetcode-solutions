class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:


        max_len = 0
        cur_len = 0
        order = ["a", "e", "i", "o", "u", ""]
        cur_letters = ["a", ""]
        for idx, ch in enumerate(word):
            if ch not in cur_letters:
                cur_len = 0
                cur_letters = ["a", ""]
                if ch == "a":
                    cur_letters[1] = "e"
                    cur_len += 1
            elif ch == cur_letters[0]:
                if ch == "a":
                    cur_letters[1] = "e"
                cur_len += 1
            elif ch == cur_letters[1]:
                cur_letters[0] = ch
                cur_letters[1] = order[order.index(ch) + 1]
                cur_len += 1
            if ch == "u" and cur_len > 0:
                max_len = max(max_len, cur_len)
        return max_len



        
