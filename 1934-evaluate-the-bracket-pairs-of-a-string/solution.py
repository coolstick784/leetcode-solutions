class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        map_dict = {}
        for key, value in knowledge:
            map_dict[key] = value

        cur = False
        res = ""
        cur_word = ""
        for idx, ch in enumerate(s):
            if ch == "(":
                cur = True
            elif ch == ")":
                if cur_word in map_dict:
                    res += map_dict[cur_word]
                else:
                    res += "?"
                cur = False
                cur_word = ""
            elif cur:
                cur_word += ch
            else:
                res += ch
        return res
