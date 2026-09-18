class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        orders = permutations("abc")
        res = "Z" * 400
        def add(cur, s):
            for idx, ch in enumerate(cur):
                used = len(cur) - idx
                if s == cur[idx:idx+len(s)]:
                    return cur
                if s.startswith(cur[idx:]):
                    return cur + s[used:]

            return cur + s
        for o in orders:
            cur = ""
            for idx, ch in enumerate(o):
                s = None
                if ch == "a":
                    s = a
                elif ch == "b":
                    s = b
                else:
                    s = c
                if cur == "":
                    cur += s
                else:
                 
                    cur = add(cur, s)
                   

            if len(cur) < len(res):
                res = cur
            elif len(cur) == len(res):
                res = min(res, cur)
        return res
